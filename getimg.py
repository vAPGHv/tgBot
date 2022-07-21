import json
import re
import requests
from bs4 import BeautifulSoup
from random import choice


def getimg(req):
    links = []

    name = req

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.85'}
    r = requests.get(f"https://www.google.com/search?q={name}&client=opera-gx&hs=XcT&sxsrf=ALiCzsYXEnUBcedkSFWmbdVAf4CQWDuzew:1658225914940&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiU2vf03IT5AhXRi8MKHcTfC5UQ_AUoAXoECAIQAw&biw=2519&bih=1330&dpr=1#imgrc=kUIe1rLXX0NjAM", headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")
    dd = soup.find('script', string=re.compile("key: 'ds:1'")).text.strip()[20:-2]
    dd = dd.replace(": '", ': "').replace("',", '",').replace('key:', '"key":').replace('hash:', '"hash":').\
        replace('data:', '"data":').replace('sideChannel:', '"sideChannel":')

    z = json.loads(dd)

    for img_links in z['data'][31][0][12][2]:
        try:
            url, _, __ = img_links[1][3]
            links.append(url)
        except Exception:
            continue

    link = choice(links)

    photo = requests.get(link).content

    with open("img.jpg", "wb") as f:
        f.write(photo)
