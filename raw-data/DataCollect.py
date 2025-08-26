import pandas as pd
from tqdm import tqdm
from TubeCrawl import downlaodPlaylist, downloadChannel

csv_dir = "/home/red/Documents/Webworm-AI-Streamer/video_urls.csv"
audio_save_dir = "/home/red/Documents/data"

df = pd.read_csv(csv_dir)

for index, row in tqdm(df.iterrows(), total=df.shape[0]):
  if row['type'] == "playlist":
    downlaodPlaylist(row['url'], audio_save_dir)
  if row['type'] == "channel":
    downloadChannel(row['url'], audio_save_dir)
