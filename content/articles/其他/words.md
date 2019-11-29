Title: Mac 在桌面上显示英语单词并自动更新
Category: 其他
Date: 2019-11-29 13:42:59
Modified: 2019-11-29 13:42:59
Tags: Mac

### 1. 爬取单词

首先第一步利用爬虫爬取了六级词汇的音标和释义。

```
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

def find_all_links():
    # A-Z
    url = 'https://cet6.koolearn.com/20171229/817624.html'
    source_code = requests.get(url , headers=headers).text
    soup = BeautifulSoup(source_code, 'html.parser')
    # 获得所有的链接
    links = []
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        link = tds[0].find('a')['href']
        links.append(link)
    return links

def find_all_pages(link):
    source_code = requests.get(link, headers=headers)
    source_code.encoding = 'utf-8'
    soup = BeautifulSoup(source_code.text, 'html.parser')
    # 获得所有页面的链接
    pages = set()
    pages.add(link)
    for page in soup.find('div',{'class':'pgbar pg'}).find_all('a'):
        if page.text:
            pages.add(page['href'])

    return list(pages)

def find_all_words(page):
    source_code = requests.get(page, headers=headers)
    source_code.encoding = 'utf-8'
    soup = BeautifulSoup(source_code.text, 'html.parser')
    core = soup.find('div',{'class':'xqy_core_text'})
    # 获得所有单词
    words = []
    for p in core.find_all('p'):
        if p.text and '/' in p.text:
            temp = p.text.replace("\u3000","").replace(" ","").split('/')
            words.append(temp)

    return words

words = []
links = find_all_links()
for link in links:
    pages = find_all_pages(link)
    for page in pages:
        words += find_all_words(page)

output = open('data.txt','w',encoding='utf-8')
for row in words:
    row_text = '{}={}={}'.format(row[0],row[1],row[2])
    output.write(row_text)
    output.write('\n')
output.close()
```

### 2. 为图片添加单词

```
# -*- coding: UTF-8

import os, sys
import shutil
from datetime import datetime
sys.path.append('/Users/xususu/anaconda3/lib/python3.6/site-packages/')
sys.path.append('/Users/xususu/anaconda3/lib/python3.6/site-packages/cv2')
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

def generator_pic(word, index):
    # 删除原来的图像
    shutil.rmtree("/Users/xususu/PycharmProjects/picword/pics/")  # 能删除该文件夹和文件夹下所有文件
    os.mkdir("/Users/xususu/PycharmProjects/picword/pics/")
    bk_img = cv2.imread("/Users/xususu/PycharmProjects/picword/test.jpg")
    # 设置需要显示的字体
    fontpath = "/Library/Fonts/Times New Roman.ttf"
    fontpath2 = "/Library/Fonts/Microsoft/SimSun.ttf"
    font = ImageFont.truetype(fontpath, 200)
    font2 = ImageFont.truetype(fontpath2, 120)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    #绘制文字信息
    draw.text((500, 300),  word[0], font = font, fill = (0, 0, 0))
    draw.text((650, 600),  "/" + word[1] + "/", font = font, fill = (0, 0, 255))
    draw.text((900, 900),  word[2], font = font2, fill = (0, 0, 0))
    bk_img = np.array(img_pil)
    cv2.imwrite("/Users/xususu/PycharmProjects/picword/pics/pic" + str(index) + ".jpg",bk_img)

origin_day = datetime(2019, 11, 29, 0, 10, 0)
present_day = datetime.now()
five_minutes_diff = int((present_day-origin_day).total_seconds()/300)
f = open("/Users/xususu/PycharmProjects/picword/data.txt", encoding="utf-8")
lines = f.readlines()
f.close()
lines = sorted(set(lines))

# 本次选取哪一个单词
index = five_minutes_diff % len(lines)
word = lines[index].split('=')
generator_pic(word, index)
print(str(index))
```

### 3. 编写脚本

```
x=$(/Users/xususu/anaconda3/bin/python3 /Users/xususu/PycharmProjects/picword/gen.py)
y='tell application "Finder" to set desktop picture to POSIX file "/Users/xususu/PycharmProjects/picword/pics/pic'${x}'.jpg"'
osascript -e "${y}"
```

### 4. 自动执行

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
        "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<!-- Created: 170925 -->

<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.xususu.mywords</string>

    <key>ProgramArguments</key>
    <array>
        <string>/Users/xususu/bin/mywords</string>
    </array>

    <key>StartInterval</key>
    <integer>300</integer>

    <key>StandardErrorPath</key>
    <string>/usr/local/var/log/mywords.txt</string>
    <key>StandardOutPath</key>
    <string>/usr/local/var/log/mywords.log</string>

</dict>
</plist>
```

放在 `/Users/xususu/Library/LaunchAgents/com.xususu.mywords.plist`。并在终端执行 `launchctl load ~/Library/LaunchAgents/com.xususu.mywords.plist`。
