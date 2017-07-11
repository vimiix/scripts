#coding=utf-8
#
#**************************************
# 文件名:baidu-image-crawler.py
# 功能：实现根据关键词自动下载百度图片
# 作者：vimiix
#***************************************

from urllib2 import Request, urlopen
import os
import re
import requests

BAIDU_IMAGE = 'http://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word='

usr_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        }

def image_crawler(kw):
    url = BAIDU_IMAGE + kw
    #print url
    req = Request(url, headers=usr_agent)
    html = urlopen(req).read()
    #print html
    images = re.findall('"objURL":"(.*?)"', html, re.S)

    counter = 0
    for img in images:
        try:
            rs = requests.get(img)
            if not os.path.exists('./images'):
                os.makedirs('./images')
            with open('./images/img'+str(counter)+'.jpg', 'wb') as f:
                f.write(rs.content)
                counter += 1
        except:
            print("img{0}'s url error".format(counter))
            continue

    return False

if __name__ == '__main__':
    run = True
    while run:
        keyword = raw_input('请输出要检索的图片关键词：')
        run = image_crawler(keyword)
