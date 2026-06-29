# Taksi Scraper Bot

## Ishga tushirish tartibi

### 1. my.telegram.org dan API kalitlar olish
- API_ID va API_HASH oling

### 2. Session string yaratish (local)
```bash
pip install pyrogram tgcrypto
python generate_session.py
```

### 3. Railway environment variables
```
API_ID=...
API_HASH=...
SESSION_STRING=...
SOURCE_GROUPS=-1001234,-1005678
TARGET_GROUP=-1009999
```

### 4. GitHub ga push → Railway avtomatik deploy
