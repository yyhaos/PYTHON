import requests
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.rcParams['font.family']='STSong'
end_data_year=2018
end_data_month=4
start_data_year=2017
start_data_month=1
dates = []
for i in range (start_data_year,end_data_year+1):
    for j in range (1,13):
        if(i==start_data_year and j<start_data_month):
            continue;
        if(i==end_data_year and j==end_data_month+1):
            break;
        dates.append(i*100+j)
#print (datas)
#-----------------------------------------
weather = []
tem_weather = ()
#-----------------------------------------
writer = pd.ExcelWriter('weather_in_BJ.xlsx')

#df.to_excel(writer, 'Data 1')


title = ['日期','最高气温','最低气温','天气','风向','风力']
for date in dates:
    #print(date)
    html = requests.get("http://lishi.tianqi.com/beijing/"+str(date)+".html",headers = head)
    from bs4 import BeautifulSoup
    bsObj = BeautifulSoup(html.content,'lxml')
    ul = bsObj.find('div' ,class_="tqtongji2")
    ass = ul.find_all('li')
    th=0
    for li in ass:
        th+=1
        tem_weather+=(li.get_text(),)
        if th == 6:
            tem_weather = ()
            continue
        if th%6==0 :
            weather.append(tem_weather)
            tem_weather = ()
    Data_1 = np.array(weather)
    Data = pd.DataFrame(Data_1,columns=title)
    
    sheet='北京'+str(int(date/100))+'年'+str(int(date%100))+'月份天气详情'
    print(sheet)
    Data.to_excel(writer,sheet,float_format='%d')
    weather = []
writer.save()
#    if(th==1188):
#       break

#print(weather)
#os.system("大作业爬取版读取绘图.py")

