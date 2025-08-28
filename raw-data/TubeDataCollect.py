'''
Since crawling through bilibili.com is not perfectly stable, this script would only uniformly collect the audio contents
from YouTube. Crawling at bilibili.com would be realized in separeted scripts.
'''

import pandas as pd
from tqdm import tqdm
from crawlers.TubeCrawl import getAudioFromPlaylist, getAudioFromChannel
from VarMap import AUDIO_SAVE_ADDRESS

# Unitilize csv to store the url of playlists and channels
csv_dir = "/home/red/Documents/Webworm-AI-Streamer/video_urls.csv"

df = pd.read_csv(csv_dir)

if __name__ == "__main__":
  for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    if row['type'] == "playlist":
      getAudioFromPlaylist(row['url'], AUDIO_SAVE_ADDRESS)
    if row['type'] == "channel":
      getAudioFromChannel(row['url'], AUDIO_SAVE_ADDRESS)
