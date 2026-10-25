# スマホ1台・Termuxで24時間完全自律稼働する「全自動トレンド収集＆サマリーボット」パッケージ v1.0

ご購入いただき誠にありがとうございます！
本パッケージは、Androidスマートフォン上のLinux環境（Termux）を活用し、PC不要・電気代ほぼゼロで24時間365日自律稼働する情報収集＆要約エンジンの完全版ソースコード一式です。

---

## 📦 パッケージ内容
1. `setup.sh` : 必要なパッケージ（Python, Git, Cronie等）を一括インストールする自動環境構築スクリプト
2. `bot_engine.py` : 世界中のRSS・トレンドニュースを自動収集し、構造化ログ・サマリーを生成するコアエンジン
3. `config.py` : 収集先RSSや動作インターバルを自由にカスタマイズできる設定ファイル
4. `run_patrol.sh` : cron（定期実行）用のバックグラウンド起床シェルスクリプト

---

## 🚀 クイックスタート（3ステップで即稼働）

### ステップ1: Termuxで本フォルダを展開
```bash
unzip termux_autonomous_bot_v1.0.zip -d ~/autonomous_bot
cd ~/autonomous_bot
```

### ステップ2: セットアップスクリプトの実行
```bash
chmod +x setup.sh run_patrol.sh
./setup.sh
```

### ステップ3: 動作テストとcron定期実行
```bash
# 即時テスト実行
python bot_engine.py

# 4時間ごとの自動巡回を登録
crontab -e
# 以下の1行を末尾に追加して保存
0 */4 * * * /data/data/com.termux/files/home/autonomous_bot/run_patrol.sh >> /data/data/com.termux/files/home/autonomous_bot/cron.log 2>&1
```

---

## 💼 商用利用・改変について
本パッケージのコードは購入者様ご自身の事業・ブログ・案件での商用利用、改変、再利用が完全に認められています。
ぜひご自身のビジネスや自動化ライフにご活用ください！
