# -*- coding: utf-8 -*-
"""Configuration for Autonomous Bot Engine"""
import os
from pathlib import Path

BASE_DIR = Path.home() / "autonomous_bot"
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

for d in [DATA_DIR, LOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "bot_database.db"

# 巡回対象のRSSフィードリスト（自由に追加・編集可能）
RSS_FEEDS = [
    "https://hnrss.org/frontpage",
    "https://github.blog/feed/",
    "https://zenn.dev/feed",
    "https://gigazine.net/news/rss_2.0/",
    "https://www.publickey1.jp/atom.xml",
]
