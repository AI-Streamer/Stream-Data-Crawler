from pytubefix import Channel, Playlist, YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import VideoUnavailable
from tqdm import tqdm

def downloadChannel(c_url, data_dir):
  channel = Channel(c_url)

  for video in tqdm(channel.videos):
    # print(video.title)
    try:
        content = video.streams.get_audio_only()
    except VideoUnavailable:
        pass  # Skip videos that can't be loaded
    else:
        content.download(output_path=data_dir)
    

def downlaodPlaylist(p_url, data_dir):
  pl = Playlist(p_url)

  for video in tqdm(pl.videos):
    # print(video.title)
    try:
        content = video.streams.get_audio_only()
    except VideoUnavailable:
        pass  # Skip videos that can't be loaded
    else:
        content.download(output_path=data_dir)


if __name__ == "__main__":
  c_url = "https://www.youtube.com/@addoil111"
  p_url = "https://www.youtube.com/watch?v=XM3FH6xnZmQ&list=PLyiDa6SkK1QQ6jeHKsHdf4t64A84x0Fji&index=2"
  data_dir = "/Users/dongyueqi/Documents/audio_test"
  downlaodPlaylist(p_url, data_dir)
  # downloadChannel(c_url, data_dir)
