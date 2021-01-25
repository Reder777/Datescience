#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: reder
#2021.1.20

import jieba
from nltk.corpus import stopwords

def keyword(filename):
    txt=open(filename,'r',encoding='utf-8').read()
    words=jieba._lcut(txt)
    counts={}
    for word in words:
        if len(word)==1:
            continue
        else:
            counts[word]=counts.get(word,0)+1
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(50):
        word,count=items[i]
        print('{0:<10}{1:>5}'.format(word,count))

def read_file(filename):
    stop = [line.strip() for line in open('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\stopword.txt', 'r', encoding='utf-8').readlines()]  # 停用词
    f = open(filename, 'r', encoding='utf-8')
    line = f.readline()
    str = []
    while line:
        s = line.split('\t')
        fenci = jieba.cut(s[0], cut_all=False)  # False默认值：精准模式
        str.append(list(set(fenci) - set(stop)))
        line = f.readline()
    return str

keyword('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_first.csv')
keyword('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_second.csv')
keyword('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_third.csv')
keyword('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_fourth.csv')