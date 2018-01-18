'''
Created on 2018年1月13日

@author: Administrator
'''
import string
from urllib import request
from urllib.parse import quote

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        
        myurl = quote(url, safe = string.printable)
        response = request.urlopen(myurl)
        
        if response.getcode() != 200:
            return None
        
        return response.read().decode('utf-8')
        