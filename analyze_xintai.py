#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from nltk.probability import  FreqDist,ConditionalFreqDist
from nltk.metrics import  BigramAssocMeasures
import jieba
from snownlp import SnowNLP

def get(filename):
    txt = open(filename, 'r', encoding='utf-8').readline()
    score=[]
    a=0
    average=0
    for i in range(0,len(txt)):
        score.append(SnowNLP(txt[i]).sentiments)
    print(score)
    for k in range(0,len(score)):
        a=a+score[k]
    average=a/len(score)
    print(average)
get('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_first.csv')
get('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_second.csv')
get('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_third.csv')
get('C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_fourth.csv')