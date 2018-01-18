'''
Created on 2018年1月14日

@author: Administrator
'''
# import osfrom os import path
import matplotlib.pyplot as plt
import numpy as np

# from scipy.misc import imread

from  wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')


text_from_local = open('worldcloude.txt').read().encode('utf-8')

world_list_after_jieba = jieba.cut(text_from_local, cut_all = True)
wl_space_split = " ".join(world_list_after_jieba)

my_cloudWorld = WordCloud().generate(wl_space_split)

plt.imshow(my_cloudWorld)
plt.axis("off")
plt.show()
