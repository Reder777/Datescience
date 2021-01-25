#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: reder
#2021.1.20

import requests
import time
import re
import catch_comments
import urllib3


class news():
    url='https://m.weibo.cn/api/container/getIndex?uid=2028810631&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%96%B0%E6%B5%AA%E6%96%B0%E9%97%BB&type=uid&value=2028810631&containerid=1076032028810631&'
    headers={
        'cookie': 'SCF=Ag5TrgLk5sHEFdW0OmwFzk0x-rTjSHHqcayifsjGMX9DZU6gtIKyqc8lKiPpFOy3RxqKlOzVWWuOLIaJeGoMqQ4.; SUB=_2A25NA6BuDeRhGeNM71YQ9SzKyTyIHXVuD8AmrDV6PUJbktAKLRHAkW1NTgmcFkg-5QTBqgAOBww8OhqVzEo-yNI1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhThjV6-JBiGM4DLATeNrBe5JpX5K-hUgL.Fo-EShBpSKzceo52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMfeoBXeK-ESoz7; ALF=1613716798; _T_WM=97842197674; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=c1795d; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E6%2596%25B0%25E6%25B5%25AA%25E6%2596%25B0%25E9%2597%25BB%26oid%3D2310022028810631_-_HOTMBLOG%26fid%3D1005052028810631%26uicode%3D10000011',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
    }
    target_words=['无症状感染','新冠肺炎','疫情防控','核酸检测','新型冠状病毒','新冠疫苗','冠状型肺炎','肺炎','新冠检测']
    params={
        'uid': 2028810631,
        't': 0,
        'luicode': 10000011,
        'lfid': '100103type = 1 & q = 新浪新闻',
        'type': 'uid',
        'value': 2028810631,
        'containerid': 1076032028810631,
        'since_id':4513875313449618,
    }
    num=0
    text=''
    date=''
    id=''
    analyzed_date=0
    all_data=[]
    dic={
        'Jan':0,
        'Dec':334,
        'Feb':31,
        'Mar':60,
        'Apr':91,
        'Oct':0,
        'Sep':0,
        'Aug':0,
        'Nov':0,
        'Jul':0,
        'May':120,
        'Jun':151,
    }
    first_stage=[]
    second_stage=[]
    third_stage=[]
    fourth_stage=[]

    def catch_news(self,n):
        count=80
        num1,num2,num3,num4=0,0,0,80
        while count<n:
            u=self.url+'since_id='+str(self.params['since_id'])
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            try:
                res = requests.get(u,headers=self.headers,verify=False)
                self.params['since_id'] = res.json()['data']["cardlistInfo"]['since_id']
                print(self.params['since_id'])
            except IOError as e:
                print(e)
                print('error')
                print(self.params['since_id'])
            l=len(res.json()['data']['cards'])
            for j in range(0,l):
                if res.json()['data']['cards'][j]['card_type']==9:
                    self.text=res.json()['data']['cards'][j]['mblog']['text']
                    self.date=res.json()['data']['cards'][j]['mblog']['created_at']
                    self.id=res.json()['data']['cards'][j]['mblog']['id']
                    text = re.sub('<.*?>', '', self.text)
                    self.analyzed_date=self.analyze_date(self.date)
                    for k in range(0,len(self.target_words)):
                        if text.__contains__(self.target_words[k]):
                            if(self.analyzed_date>334)or((self.analyzed_date>1)and(self.analyzed_date)<=181):
                                self.all_data.append(self.date)
                                self.all_data.append(self.analyzed_date)
                                self.all_data.append(self.id)
                                print(self.id,end='kkk')
                                print(self.analyzed_date)
                                count=count+1
                                instance = catch_comments.weibo()
                                if (self.analyzed_date>334)or(self.analyzed_date<22):
                                    if (num1 <= 100):
                                        catch_comments.weibo().catch(30, news().all_data[2], news().all_data[0],news().all_data[1],'C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_first.csv')
                                    else:
                                        count=count-1
                                    num1=num1+1
                                if (self.analyzed_date>=22)and(self.analyzed_date<41):
                                    if (num2 <= 100):
                                        catch_comments.weibo().catch(30, news().all_data[2], news().all_data[0], news().all_data[1],'C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_second.csv')
                                    else:
                                        count=count-1
                                    num2=num2+1
                                if (self.analyzed_date>=41)and(self.analyzed_date<70):
                                    if (num3 <= 100):
                                        catch_comments.weibo().catch(30, news().all_data[2], news().all_data[0], news().all_data[1],'C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_third.csv')
                                    else:
                                        count=count-1
                                    num3=num3+1
                                if (self.analyzed_date>=70)and(self.analyzed_date<=181):
                                    if(num4<=100):
                                        catch_comments.weibo().catch(30, news().all_data[2], news().all_data[0], news().all_data[1],'C:\\Users\\芮宏宇\\PycharmProjects\\爬虫\\weibocomments_fourth.csv')
                                    else:
                                        count=count-1
                                    num4=num4+1
                                self.all_data.clear()
                                break
            time.sleep(2)

    def analyze_date(self,date):
        i=0
        temp=date.split(' ')
        if (temp[5]!='2020')and(temp[5]!='2019'):
            return -100000
        i=i+self.dic[temp[1]]+int(temp[2])
        return i

if __name__ == '__main__':
    news().catch_news(400)
