#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autonomous Bot Core Engine
World Trend Collector & SQLite Logger
"""
import sys
import time
import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import config

def init_db():
    with sqlite3.connect(config.DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS feeds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                url TEXT UNIQUE,
                source TEXT,
                summary TEXT,
                published_at TEXT,
                created_at TEXT
            )
        """)
        conn.commit()

def collect_feeds():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting feed collection...")
    init_db()
    total_new = 0

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    with sqlite3.connect(config.DB_PATH) as conn:
        c = conn.cursor()
        for feed_url in config.RSS_FEEDS:
            try:
                res = requests.get(feed_url, headers=headers, timeout=15)
                if res.status_code != 200:
                    continue
                soup = BeautifulSoup(res.content, "xml")
                items = soup.find_all(["item", "entry"])
                for item in items:
                    title_el = item.find("title")
                    link_el = item.find("link")
                    title = title_el.get_text(strip=True) if title_el else ""
                    if link_el:
                        url = link_el.get("href") or link_el.get_text(strip=True)
                    else:
                        url = ""
                    if not title or not url:
                        continue
                    try:
                        c.execute("""
                            INSERT INTO feeds (title, url, source, summary, published_at, created_at)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (title, url, feed_url, "", "", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        total_new += 1
                    except sqlite3.IntegrityError:
                        pass
            except Exception as e:
                print(f"Error fetching {feed_url}: {e}")
        conn.commit()

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Collection finished. New items: {total_new}")

if __name__ == "__main__":
    collect_feeds()
