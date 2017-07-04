#_*_coding:utf8_*_
#
# 文件名：csdn_blog_column_list.py
# 功能：爬取csdn博客专栏标题和链接,
#       输出到当前文件夹的List.xls中
# 使用方式：
#       python blog_column_list.py <目标链接> <页数>
# 环境：python2.7.13
# 作者：vimiix
#####################工作用#####################


import urllib2,urllib
from bs4 import BeautifulSoup
import os
import sys
import xlwt



class csdnArtical(object):

    def __init__(self,des_url, page_num = 1):
        self.article_info = []    
        self.page_url = des_url  
        self.page_num = int(page_num)
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}

    def __request(self,url):
        self.url = url  
        self.req = urllib2.Request(url=self.url,headers=self.header)        #url的request请求头
        self.page_info = urllib2.urlopen(self.req).read().decode('utf-8')   #html的源码
        self.soup = BeautifulSoup(self.page_info,'html.parser')             #实例化soup对象，以bs4的格式化实现
        return self.soup                  

    def _get_artical_info(self):
        for _ in range(1,self.page_num+1):
            soup = self.__request(self.page_url+"?&page="+str(_))
            ul = soup.find('ul', attrs={"class": "detail_list"})
            a_list = ul.find_all('a')  
            for a in a_list:
                try:
                    title = a.text
                    #print title
                    url = a['href']
                    Info = (title, url)
                    self.article_info.append(Info)
                except Exception as e:
                    pass

    def saveArticalInfo(self,save_path):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('blog_articleInfo')
        self.save_path = save_path
        self._get_artical_info()
        line = 1
        if self.article_info:
            for info in self.article_info:
                ws.write(line, 0, info[0])
                ws.write(line, 1, info[1])
                print ('Line%s saved...'%line)
                line += 1
            wb.save(self.save_path)
        else:
            print 'Warning: Get nothing!!!!'

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        url = sys.argv[1]
        pages = sys.argv[2]
        blog_artical = csdnArtical(des_url=url,page_num=pages)
        savePath = 'List.xls'
        blog_artical.saveArticalInfo(savePath)
    else:
        print ("Please input des link.~-~\nUsage:{} <colum_link> <paginal number>").format(sys.argv[0])

