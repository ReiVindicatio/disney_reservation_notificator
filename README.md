# disney_reservation_notificator
予約キャンセルを検知しdiscordに通知

cron などを使えば定期的に取得が可能

## 前提
- poetry がインストールされていること
- discord の webhook url が作成済み

## 使い方
1. クローンしたフォルダで仮想環境を設定
```bash
> poetry install
```

仮想環境を作成する前に `poetry config --local virtualenvs.in-project true` をしておくと仮想環境がプロジェクト直下にできて便利

2. discord の Webhook を作成し、.app-env に設定
```bash:.app-env
# --------------------------------------
# Discord 
# --------------------------------------
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/0000000000000000000/xxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 上記を取得した Webhook のURLに書き換える
# webhook の取得方法は頑張って調べる
```

**注意** webhook の URL を push しないように

3. config.yaml の設定
監視したい日付 `use_date`、人数 `adult_num`および監視対象を `config.yaml` に設定する。<br/>
例） 2025/06/10の二人、ファンタジースプリングホテルの【ファンタジーシャトー】ベイサイドエリアのみを監視したい場合：
```yaml:config.yaml
config:
  reservation:
    hotel:
      metadata:
        use_date: "20250610"
        adult_num: 2
      hotels:
        - hotel_id: "100"
          logical_name: "東京ディズニーシー・ファンタジースプリングスホテル"
          is_monitored: true
          rooms:
            - room_id: "101"
              logical_name: "【ファンタジーシャトー】ベイサイドエリア"
              is_monitored: true
            - room_id: "102"
              logical_name: "【ファンタジーシャトー】ホテルエントランスサイド"
              is_monitored: false
            - room_id: "103"
              logical_name: "【ファンタジーシャトー】ローズコードサイド"
              is_monitored: false
            - room_id: "104"
              logical_name: "【ファンタジーシャトー】スプリングスサイド"
              is_monitored: false
            ...
```

4. 実行する
```bash
> cd disney_reservation_notificatior
> poetry run python main.py
```