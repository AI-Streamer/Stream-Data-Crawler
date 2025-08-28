from pytubefix import Channel, Playlist, YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import VideoUnavailable
from tqdm import tqdm


def getAudioFromChannel(c_url, data_dir):
  channel = Channel(c_url)

  for video in tqdm(channel.videos):
    # print(video.title)
    try:
        content = video.streams.get_audio_only()
    except VideoUnavailable:
        pass  # Skip videos that can't be loaded
    else:
        content.download(output_path=data_dir)


def getAudioFromPlaylist(p_url, data_dir):
  pl = Playlist(p_url)

  for video in tqdm(pl.videos):
    # print(video.title)
    try:
        content = video.streams.get_audio_only()
    except VideoUnavailable:
        pass  # Skip videos that can't be loaded
    else:
        content.download(output_path=data_dir)

