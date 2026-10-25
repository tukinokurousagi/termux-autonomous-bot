#!/data/data/com.termux/files/usr/bin/bash
echo "[*] Setting up Termux Autonomous Bot Environment..."
pkg update -y && pkg upgrade -y
pkg install -y python git cronie sqlite curl jq
pip install --upgrade pip
pip install requests beautifulsoup4 jinja2 markdown2
termux-wake-lock
echo "[+] Setup successfully completed!"
