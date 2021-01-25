#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: reder
#2021.1.20

import re
import time
import requests
import os

class weibo():
    url="https://m.weibo.cn/comments/hotflow?"
    headers={
        'cookie':'SCF=Ag5TrgLk5sHEFdW0OmwFzk0x-rTjSHHqcayifsjGMX9DZU6gtIKyqc8lKiPpFOy3RxqKlOzVWWuOLIaJeGoMqQ4.; SUB=_2A25NA6BuDeRhGeNM71YQ9SzKyTyIHXVuD8AmrDV6PUJbktAKLRHAkW1NTgmcFkg-5QTBqgAOBww8OhqVzEo-yNI1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhThjV6-JBiGM4DLATeNrBe5JpX5K-hUgL.Fo-EShBpSKzceo52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMfeoBXeK-ESoz7; ALF=1613716798; _T_WM=97842197674; XSRF-TOKEN=881ec1; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E6%2596%25B0%25E9%2597%25BB%26fid%3D1076032028810631%26uicode%3D10000011',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'
    }
    max_id=0
    max_id_type=0
    comment_list=[]
    params={
        'id': None,
        'mid': None,
        'max_id':max_id,
        'max_id_type': max_id_type
    }
    file_loc='./data'
    date=''
    analyzed_date=0



    def catch(self,num,id,date,analyzed_date,name):
        self.params['id'],self.params['mid']=id,id
        self.date=date
        self.analyzed_date=analyzed_date
        i=0
        while i <num:
            try:
                resq=requests.get(url=self.url,headers=self.headers,params=self.params)
            except IOError as e:
                print(e)
            self.params['max_id'],self.params['max_id_type']=resq.json()['data']['max_id'],resq.json()['data']['max_id_type']
            for k in range(0,len(resq.json()['data']['data'])):
                self.comment_list.append(resq.json()['data']['data'][k]['text'])
            self.parse_data()
            self.write_csv(name)
            self.clear()
            i=i+1
            time.sleep(2)
            if(self.params['max_id']==0):
                break


    def parse_data(self):
        for i in range(0,len(self.comment_list)):
            self.comment_list[i]=re.sub('<.*?>','',self.comment_list[i])

    def write_csv(self,name):
        open(name,'a',encoding='utf-8').write('%s_%d\n'%(self.date,self.analyzed_date))
        with open(name,'a',encoding='utf-8') as fp:
            for i in self.comment_list:
                fp.write('%s\n'%i)

    def clear(self):
        self.comment_list.clear()





