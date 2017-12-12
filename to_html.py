# coding=utf-8

import os
from pyhtml import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

str_style = '''
body.rpt  {font:bold 10pt Arial,Helvetica,Geneva,sans-serif;color:black; background:White;}
pre.rpt  {font:8pt Courier;color:black; background:White;}
h1.rpt   {font:bold 20pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;border-bottom:1px solid #cccc99;margin-top:0pt; margin-bottom:0pt;padding:0px 0px 0px 0px;}
h2.rpt   {font:bold 18pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}
h3.rpt {font:bold 16pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}
li.rpt {font: 8pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;}
h4.rpt {font:bold 10pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}
li.rpt {font: 8pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;}
h5.rpt {font:10pt Arial,Helvetica,Geneva,sans-serif;color:black;background-color:White;margin-top:4pt; margin-bottom:0pt;}
li.rpt {font: 8pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;}
th.rptnobg {font:bold 8pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;padding-left:4px; padding-right:4px;padding-bottom:2px}
th.rptbg {font:bold 8pt Arial,Helvetica,Geneva,sans-serif; color:White; background:#0066CC;padding-left:4px; padding-right:4px;padding-bottom:2px}
td.rptnc {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;}
td.rptc    {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;}
td.rptcc {font:8pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background:White;vertical-align:top;}
a.rpt {font:bold 8pt Arial,Helvetica,sans-serif;color:#663300; vertical-align:top;margin-top:0pt; margin-bottom:0pt;}
a.rptnb {font:8pt Arial,Helvetica,sans-serif;color:#663300; vertical-align:top;margin-top:0pt; margin-bottom:0pt;text-decoration:none}
'''

class ToHtml():

    def __init__(self, title, base_info):
        self.title = title
        self.base_info = base_info
        self.html = None

    def make_html(self):
        '''生成html源码结构'''
        self.html = html(
            head(
                title(self.title),
                style(str_style)
            ),
            body(class_='rpt')(
                h1(class_='rpt')('MySQL数据库巡检报告'),
                p(
                    table(border=0, width=600)(
                        tr(
                            td(class_='rptcc')('客户名称:'),
                            td(class_='rptcc')('%s'%self.base_info['custname'])
                        ),
                        tr(
                            td(class_='rptcc')('合同号:'),
                            td(class_='rptcc')('%s'%self.base_info['contract_num'])
                        ),
                        tr(
                            td(class_='rptcc')('巡检日期:'),
                            td(class_='rptcc')('%s'%self.base_info['inpection_date'])
                        ),
                        tr(
                            td(class_='rptcc')('上一次巡检日期:'),
                            td(class_='rptcc')('%s'%self.base_info['latest_inspection_date'])
                        ),
                        tr(
                            td(class_='rptcc')('巡检执行人:'),
                            td(class_='rptcc')('%s'%self.base_info['name'])
                        ),
                    ),

                    # 头部内容结束，后面的数据部分仿照上面写就好了，类似Html结构
                )
            )
        )
    def save_to_file(self, file=None):
        '''保存html文本
           :param file接受文件名或者文件夹路径,如果不传就直接在终端打印
        '''
        if file:
            path = ''
            if os.path.isfile(file):
                path = file
                with open(path, 'w') as f:
                    f.write(str(self.html))
            elif os.path.isdir(file):
                path = file + 'output.html'
                with open(path, 'w') as f:
                    f.write(str(self.html))
            else:
                print("Wrong file name or path")
                return
            print("Save html success. FilePath:%s" % path)
        else:
            print(self.html)

if __name__ == "__main__":
    baseinfo={'custname':'NASA',
              'contract_num':'888888',
              'inpection_date':'2017-12-12',
              'latest_inspection_date':'2017-12-11',
              'name':'Vimiix'}
    tohtml = ToHtml('第三季度巡检', baseinfo)
    tohtml.make_html()
    tohtml.save_to_file()
