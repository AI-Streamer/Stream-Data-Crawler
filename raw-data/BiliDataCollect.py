from tqdm import tqdm
from crawlers.BiliCrawl import getAudioFromBilibili
from VarMap import BILIBILI_URL, BILIBILI_HEADER, AUDIO_SAVE_ADDRESS

if __name__ == "__main__":
  getAudioFromBilibili(AUDIO_SAVE_ADDRESS, BILIBILI_URL, BILIBILI_HEADER)
