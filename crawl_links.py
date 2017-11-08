#coding=utf-8
"""爬取某条链接的网页内容
   run on python3.x
"""

import urllib.request
import ssl

def get_url_content(url):
    '''docstring'''

    headers = {"User-Agent":'User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
    'Chrome/61.0.3163.100 Mobile Safari/537.36'}

    try:
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, context=context).read()
        content = resp.decode('utf-8')
        print(content)
    except urllib.error.URLError as error:
        if hasattr(error, 'reason'):
            print(error.reason)

if __name__ == "__main__":
    URL = 'http://www.qiushibaike.com/'
    get_url_content(URL)

