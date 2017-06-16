# -*- coding: utf-8 -*-
import pymysql
import os
import csv
import re

def WriteToDabase(file):
    with open(file,'r+') as f:
        csvReader = csv.DictReader(f)
        for line in csvReader:
            day =line['日期']
            account_name = line['账户']
            campaign_name = line['推广计划']
            group_name = line['推广单元']
            keyword = line['关键词']
            ad_impression = line['展现量']
            ad_click = line['点击量']
            ad_cost = line['消费']
            position = line['平均排名']
            data = (day,account_name,campaign_name,group_name,keyword,ad_impression,ad_click,ad_cost,position)
            cur.execute(sql,data)
            conn.commit()

if __name__=='__main__':
    sql = 'INSERT INTO mkt_sem_keyword (day,account_name,campaign_name,group_name,keyword,ad_impression,ad_click,ad_cost,position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='mkt_sem',charset='utf8')
    cur = conn.cursor()  
    os.chdir(r'C:\Users\Administrator\Downloads')  
    filelist = os.listdir()
    pat = re.compile(r'.+\.csv')
    for file in filelist:
        ma = re.match(pat,file)
        if ma:
            WriteToDabase(file)
            os.remove(file)
    cur.close()
    conn.close()
