'''
Possibly due to the anti-crawling features applied at Bilibili, requests() function may not collect all audios at once.
Fortunately, it appears that normal crawling would not activate IP blackliting. Thus, trying to run the script for
multiple times might be help you to collect all the contents in the playlist.
'''

import requests
import re
import json
import time
import random

'''
Send request to the browser and get the titles and cid's from the returned url. Use the id's to get the source of videos
and store as audio files.
'''

def getAudioFromBilibili(audio_address, url, headers):
    response = requests.get(
        url=url,
        headers=headers
        )

    json_data = response.json()
    pages = json_data['data']['View']['ugc_season']['sections'][0]['episodes']
    count = 0

    for page in pages:
        time.sleep(random.uniform(1,3))
        title = page['title']
        bvid = page['bvid']


        link = f"https://www.bilibili.com/video/{bvid}"
        link_data = requests.get(url=link, headers=headers, verify=False)
        html = link_data.text
        info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
        link_data = json.loads(info)
        audio_url = link_data['data']['dash']['audio'][1]['baseUrl']

        resp = requests.get(url=audio_url, headers=headers)
        print(title, resp)
        # check if the request has achieved successfully
        if resp.status_code == 200:
            count += 1
            audio_content = resp.content
            with open(audio_address + title + '.mp3', mode='wb') as audio:
                audio.write(audio_content)

    print(f"Request done: {count}/{len(pages)} content has sucessfully downloaded.")
