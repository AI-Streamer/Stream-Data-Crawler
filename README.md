# Stream Data Crawler

Crawl the audio content at Vtubers and Streamers on YouTube and Bilibili.

## Usage

**Please adjust VarMap.py file in the corresponding directory before crawling raw data and generate the script from audio content.**

```
----- Stream-Data-Crawler
    ----- raw-data
        ----- crawlers
            - __init__.py
            - BiliCrawl.py
            - TubeCrawl.py
        - BiliDataCollect.py
        - TubeDataCollect.py
        - VarMap.py
    ----- script
        - ScriptRecog.py
        - VarMap.py
```

This repositiry includes raw audio data collection and audio-to-text transcription.

1. [**Raw audio data collection (crawler)**](#raw-data)
1. [**Audio transcript (FunASR)**](#transcript)

<a name="raw-data"></a>

### Raw Audio Data Collection (Crawler)

`/raw-data/VarMap.py` stores the save address, urls and headers required for crawling.

| Variable Name      | Functionality                                                             |
| ------------------ | ------------------------------------------------------------------------- |
| AUDIO_SAVE_ADDRESS | Address for saving audio file                                             |
| BILIBILI_URL       | API url address of a playlist in bilibili.com                             |
| BILIBILI_HEADER    | Header fot request audio content from Bilibili, usually no need to adjust |
| TUBE_CSV_ADDRESS   | Address to csv file strong YouTube playlist and channel urls              |

Run `BiliDataCollect.py` and `TubeDataCollect.py` to collect the content from bilibili.com and YouTube.

`TubeDataCollect.py` collects contents from bith channels and playlists. Create a csv file to store the url and type (channel or playlist). See example csv.

`BiliDataCollect.py` only collects contents from playlists. To get the api address, inspect the webpage and then click video in the playlist. You can fild a web block called "playurl", copy the requst url as the value of `BILIBILI_URL`.

![playurl](/README/playurl.gif)

\*\* Possibly due to the anti-crawler features of bilibili.com, the `requests()` function utilized in `BiliDataCollect.py` might not collect all the contents in the playlist. You can try to run the file multiple times to collet all the contents.

<a name="transcript"></a>

### Audio Transcript (FunASR)

Audio transcription is developed based on [FunASR](https://github.com/modelscope/FunASR). You can check the original repository at https://github.com/modelscope/FunASR.

`/script/VarMap.py` stores the saving address and model directory required for AI-based audio-to-text recognition.

| Variable Name       | Functionality                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| AUDIO_SAVE_ADDRESS  | Address to saved audio file                                                                       |
| SCRIPT_SAVE_ADDRESS | Address for saving audio transcripts                                                              |
| MODEL_DIRECTORY     | Directory to access the ASR models. The directory can be local or from huggingface/modelscope hub |
