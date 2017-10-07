#coding=utf-8
"""自动下载对应专辑编号内的所有资源名称和链接
   用法：python csdn_album_src_info.py 专辑编号1 [专辑编号2 ....]
"""
__author__ = 'Vimiix'

import os
import sys
import urllib2
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

SAVEPATH = os.path.dirname(os.path.realpath(__file__)) + '/albums/'

class AlbumDownloader(object):
    '''专辑名称链接自动下载'''

    def __init__(self, album_index, save_file):
        self.page_total = 1
        self.result = []
        self.base_url = "http://download.csdn.net/album/detail/"+str(album_index)
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}
        if not os.path.exists(SAVEPATH):
            os.mkdir(SAVEPATH)
        self.file_path = SAVEPATH + save_file

    def auto_down(self):
        '''下载入口'''
        self._get_album_src()
        if self.result:
            with open(self.file_path, 'w') as fp:
                for line in self.result:
                    fp.write(line)
            print "Download successful."
        else:
            print "Get noting, Please check your URL"

    def _get_album_src(self):
        soup = self._request(self.base_url)
        src_total = soup.find('h4', attrs={"class": 'dl_common_t'}).find('span').text
        self.page_total = int(src_total[1:3])/10 + 1
        for i in range(self.page_total):
            url = self.base_url + "/1/%d" % (i+1)
            soup = self._request(url)
            a_labels = soup.find('div', attrs={"class": "album_detail_wrap"}).find_all('a', attrs={"class":"album_detail_title"})
            for a in a_labels:
                src_url = "download.csdn.net" + a['href']
                src_title = a.text
                res_line = "|"+src_title+"|["+src_url+"]("+src_url+")|\n"
                self.result.append(res_line)

    def _request(self, url):
        req = urllib2.Request(url=url, headers=self.header)
        resp = urllib2.urlopen(req).read().decode("utf-8")
        soup = BeautifulSoup(resp, 'html.parser')
        return soup


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        for index in sys.argv[1:]:
            save_file = "album"+str(index)+".md"
            downloader = AlbumDownloader(index, save_file)
            downloader.auto_down()
    else:
        print u"缺少专辑编号\nUsage: python csdn_album_src.py album_index ..."


