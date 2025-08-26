import requests
import re
import json
import time
import random

'''
Send request to the browser and get the titles and cid's from the returned url. Use the id's to get the source of videos
and store as audio files.
'''

# the directory for saving the audio files
audio_address = "/home/red/Documents/data/"

url = "https://api.bilibili.com/x/web-interface/wbi/view/detail?aid=1355736200&need_view=1&isGaiaAvoided=false&web_location=1315873&dm_img_list=[%7B%22x%22:2901,%22y%22:2718,%22z%22:0,%22timestamp%22:106,%22k%22:77,%22type%22:0%7D,%7B%22x%22:2928,%22y%22:2741,%22z%22:16,%22timestamp%22:421,%22k%22:93,%22type%22:0%7D]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEFNRCwgQU1EIFJhZGVvbihUTSkgR3JhcGhpY3MgKDB4MDAwMDE2NEUpIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpR29vZ2xlIEluYy4gKEFNRC&dm_img_inter=%7B%22ds%22:[%7B%22t%22:2,%22c%22:%22dmlkZW8taW5mby1jb250YWluZXIgd2%22,%22p%22:[909,59,13],%22s%22:[306,2518,2868]%7D],%22wh%22:[3964,6628,108],%22of%22:[113,226,113]%7D&w_rid=21116a0f616e942a8f482c0f50d7db2c&wts=1751586758"

def getAudioFromBilibili(audio_address, url):
    #web request headers
    headers = {
        "Cookie": "buvid3=614B0A81-12A9-3E6B-14E5-2B20844DCD7B11280infoc; b_nut=1749446411; _uuid=1410143B8-21B1-2744-E3D3-BA66104649AD912648infoc; buvid_fp=505b2f1d3dcd4377687745453e2236ae; buvid4=0F738FC6-EACB-F721-A839-B0D9D85C815851103-024111714-pudptKNkP+WvehEtEZEpQw%3D%3D; rpdid=|(JRl|)kkmlY0J'u~luJR)YYJ; header_theme_version=OPEN; enable_web_push=DISABLE; home_feed_column=5; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTE3NzcwOTIsImlhdCI6MTc1MTUxNzgzMiwicGx0IjotMX0.mJzU3prB908DpQxTjfKPKqImbHXflNr8OibtaWW5W6k; bili_ticket_expires=1751777032; SESSDATA=082f4d92%2C1767070773%2Cbaa6e%2A72CjA0U9n5aUyEvfznuv90Mvm3QsN9y3dzd-WDSoeGPCB0zUvhT1vFg-SfACsmCcvU3FMSVm55elp4bmxaZGR1dWl4YjM0RlhmLVhFMkk0Z29USzFJMXJ2dTdQYThhOElqTXQwRXVSUC1FNUU2cjJzd2RVQUNPV0tndmJnSXBYSzdIQWRUTkNrRmtRIIEC; bili_jct=63cfb6e77a999edf4e4ad19d2fcab6da; DedeUserID=29408002; DedeUserID__ckMd5=4ee1bad441b73980; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; CURRENT_QUALITY=80; b_lsid=D10D13C1B_197D2B2BBFF; browser_resolution=1668-919; sid=4vwrahqo; CURRENT_FNVAL=4048; bp_t_offset_29408002=1085545815763582976",
        "Refer": "https://www.bilibili.com/video/BV1Kz421877x",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "accept-encoding": "gzip, deflate, br, zstd",
        "Accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "origin": "https://www.bilibili.com",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }

    response = requests.get(
        url=url,
        headers=headers
        )

    json_data = response.json()
    pages = json_data['data']['View']['ugc_season']['sections'][0]['episodes']

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
        if resp.status_code == 200:
            audio_content = resp.content
            with open(audio_address + title + '.mp3', mode='wb') as audio:
                audio.write(audio_content)

if __name__ == "__main__":
    getAudioFromBilibili(audio_address, url)
