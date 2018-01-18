'''
Created on 2018年1月13日

@author: Administrator
'''
#from crawer.baidubaike_Spider import *

from crawer.baidubaike_Spider import html_downloader
from crawer.baidubaike_Spider import html_outputer
from crawer.baidubaike_Spider import html_parser
from crawer.baidubaike_Spider import url_manager
#from itertools import count


class SpiderMain(object):
    def  __init__(self): # 初始化
        self.urls = url_manager.UrlManager() # url管理器
        self.downloader = html_downloader.HtmlDownloader() # 下载器
        self.parser = html_parser.HtmlParser() # 解析器
        self.outputer = html_outputer.HtmlOutputer() # 输出器
        
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                # print(html_cont[1:100])
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data) 
                
                if count >= 1000:
                    break
                
                count += 1
                
            except Exception as e:
                print('抛出的异常：' + str(e))
                # 根据报告信息提示错误
                
            self.outputer.output_html()
    
# 总的程序入口    
if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    print('Beginning~~~~~~')
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    