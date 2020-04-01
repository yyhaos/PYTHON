import requests
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib
matplotlib.rcParams['font.family']='STSong'

for i in range(2011,2018):
    #if i ==2012 :
        #break
    weather=pd.DataFrame()
    tem_weather=pd.DataFrame()
    for j in range(1,13):
        if i == 2017 and j == 12:
            continue
        sheet='北京'+str(i)+'年'+str(j)+'月份天气详情'
        tem_weather = pd.read_excel('北京天气.xls',sheet,index_col=0)
        #print(tem_weather)
        weather = pd.concat([weather,tem_weather])
    #print(weather)
    # Data_1 = np.array(weather)
    #print(Data_1)
    #print(weather.天气)
    count_list = [0 for i in range (1,8)]
    #print(count_list)
    for  day_weather in weather.天气:
        #print(i)
        if '晴' in day_weather :
            count_list[0]+=1
        if '雨' in day_weather :
            count_list[1]+=1
        if '多云' in day_weather :
            count_list[2]+=1
        if '阴' in day_weather :
            count_list[3]+=1
        if '雪' in day_weather :
            count_list[4]+=1
        if '霾' in day_weather :
            count_list[5]+=1
        if '沙尘' in day_weather :
            count_list[6]+=1
    #print(count_list)
    title = ['日期','最高气温','最低气温','天气','风向','风力']
    ned_weather = ['晴','雨','多云','阴','雪','霾','沙尘']
    
    
    #Data = pd.DataFrame(Data_1,columns=title)
    #gs = weather.groupby('天气')
    # print(gs.count())
    #coun=gs.count()#.ix[ned_weather]
    #print(coun)
    #print(coun.最高气温)
    #tem_count_list = np.array(coun.最高气温).tolist()   #转换为list
    #print(tem_count_list)
    '''
    for k in tem_count_list :
        #print(i)
        if k != k:
            count_list.append(0)
        else:
            count_list.append(int(k))
    #print(count_list)
    '''
    index_list=ned_weather
    #print(index_list)
    #---------------------------------------
    matplotlib.rcParams['font.family']='STSong'
    gs = gridspec.GridSpec(2,4)
    plt.subplot(gs[0:2,0:2])
    plt.pie(count_list,labels=index_list,autopct='%1.1f%%',shadow=True,startangle=90)
    #plt.show(pic)
    plt.text(-1,-1.3,str(i)+'年天气统计图',
             style='italic',size=15,
             bbox={'facecolor':'blue','alpha':0.5})
   # plt.savefig('图-'+str(i),dip=500)
    #plt.close('all')

    #------------------------------------------
    wumai_lab = ('1天','2天','3天','4天','5天及以上')
    wumai_days = [0 for i in range(1,6)]
    Data_1 = np.array(weather)
    #print(Data_1)
    weathers = Data_1[:,2]
    #print(weathers)
    flag = 0
    for s in weathers:
        #print(i)
        if '霾' in s:
            flag += 1
        else :
            if flag >5 :
                flag = 5
            if flag ==0 :
                continue
            wumai_days[flag-1] += 1
            flag = 0
    #plt.subplot(122)
    plt.subplot(gs[0:2,3])
    n_groups = 5
    index = np.arange(n_groups)
    bar_width = 0.5
    plt.bar(index , wumai_days,bar_width,alpha=0.4,color='b')
    #plt.xticks(n)
    plt.ylabel('次数')
    plt.xlabel('持续天数')
    plt.title(str(i)+'年雾霾持续天数统计')
    plt.xticks(index+bar_width,wumai_lab)
    plt.savefig(str(i)+'年统计',dip=500)
    #plt.show()
    plt.close('all')
    print(i)
