# yt-concatenate

## 專案概述
yt-concatenate 是一款智能影片剪輯助手，能夠自動搜尋 YouTube 頻道內含有特定英文關鍵字的影片片段，並將這些片段無縫組合成一個精彩的合輯影片。

透過分析字幕檔案，此工具能夠精確定位關鍵內容，讓您免去手動搜尋和剪輯的繁瑣過程。

## 核心功能

🔍 **智能關鍵字搜尋**：從頻道中精確找出包含特定關鍵字的所有影片段落

✂️ **自動影片擷取**：根據字幕時間碼自動裁剪相關片段

🔄 **無縫影片合併**：將所有片段組合成流暢的單一影片


### 安裝流程

```bash

git clone https://github.com/itsmeru/yt-concatenate.git

# 進入專案目錄
cd yt_concatenate

# 安裝依賴
pip install -r requirements.txt

```

### 環境變數

```bash
# YouTube API 設定
# 請從以下網址獲取 API KEY:
# https://developers.google.com/youtube/v3/getting-started?hl=zh-tw
YT_KEY = "您的API金鑰"
```

### 基本使用
```bash
# 查看相關指令
python main.py --help

# 範例
python main.py -c UC2mKA8JTOCeodl9bEK7w42Q --search_word terrible
```

### 查詢YouTube ID

參考網址： https://vocus.cc/article/65d9ddb1fd89780001e3ca95
