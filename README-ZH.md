# 流媒体数据爬虫

爬取虚拟主播和主播在 YouTube 和哔哩哔哩上的音频内容。

\[[EN](README-EN.md)|ZH\]

## 用法

**在爬取原始数据并从音频内容生成脚本之前，请先调整相应目录中的 `VarMap.py` 文件。**

```
----- Stream-Data-Crawler
    ----- raw-data
        ----- crawlers
          - init.py
          - BiliCrawl.py
          - TubeCrawl.py
        - BiliDataCollect.py
        - TubeDataCollect.py
        - VarMap.py
    ----- script
        - ScriptRecog.py
        - VarMap.py
```

该仓库包括原始音频数据采集和音频转文本。

1. [**原始音频数据采集（爬虫）**](#raw-data)
2. [**音频转写（FunASR）**](#transcript)

<a name="raw-data"></a>

### 原始音频数据采集（爬虫）

`/raw-data/VarMap.py` 存放用于爬取的保存地址、URL 和请求头信息。

| 变量名             | 功能说明                                          |
| ------------------ | ------------------------------------------------- |
| AUDIO_SAVE_ADDRESS | 用于保存音频文件的地址                            |
| BILIBILI_URL       | bilibili.com 播放列表的 API 地址                  |
| BILIBILI_HEADER    | 请求哔哩哔哩内容所用的请求头，通常无需调整        |
| TUBE_CSV_ADDRESS   | 保存 YouTube 播放列表和频道 URL 的 CSV 文件的地址 |

运行 `BiliDataCollect.py` 和 `TubeDataCollect.py`，即可分别从哔哩哔哩和 YouTube 收集内容。

`TubeDataCollect.py` 会从频道和播放列表收集内容。请创建一个 CSV 文件，存储 URL 和类型（频道或播放列表），参见示例 CSV。

`BiliDataCollect.py` 仅从播放列表收集内容。要获取 API 地址，可检查网页并点击播放列表中的视频。在网页源中找到名为 “playurl” 的区块，复制请求 URL 作为 `BILIBILI_URL` 的值。

![playurl](/README/playurl.gif)

**由于哔哩哔哩的反爬虫机制，`BiliDataCollect.py` 中使用的 `requests()` 函数可能无法收集到播放列表中的所有内容。您可以尝试多次运行该文件以收集完整内容。**

<a name="transcript"></a>

### 音频转写（FunASR）

音频转写功能基于 [FunASR](https://github.com/modelscope/FunASR) 开发。原仓库可在 https://github.com/modelscope/FunASR 查看。

`/script/VarMap.py` 存储 AI 音频转文本识别所需的保存地址和模型目录。

| 变量名              | 功能说明                                                                         |
| ------------------- | -------------------------------------------------------------------------------- |
| AUDIO_SAVE_ADDRESS  | 音频文件保存地址                                                                 |
| SCRIPT_SAVE_ADDRESS | 音频转写文本保存地址                                                             |
| MODEL_DIRECTORY     | ASR 模型所在目录，可以是本地目录，也可以是 HuggingFace/ModelScope 提供的远程目录 |

运行 `ScriptRecog.py` 将音频内容转写为文本。
**目前模型需在本地加载和部署，请根据需求选择合适的模型。**

## 未来计划

- [ ] 支持云端模型部署。
- [ ] 提供 Google Colab 示例。
