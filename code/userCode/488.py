import pandas

data = pandas.read_csv('图灵大街.csv')
data1=data['时间']
data2=data['污染指数']
data3=data['天气']
dataans=data['是否堵车']
import os


# 编写代码,计算'时间'和'是否堵车'的相关性
time_corr =date1.corr(dataans)
# 编写代码,计算'污染指数'和'是否堵车'的相关性
air_corr =os.getcwd()#date2.corr(dataans)
# 编写代码,计算'天气'和'是否堵车'的相关性
weather_corr =date3.corr(dataans)


print('时间', time_corr)
print('污染指数', air_corr)
print('天气', weather_corr)
