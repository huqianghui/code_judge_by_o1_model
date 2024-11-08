import pandas

data = pandas.read_csv('图灵大街.csv')


# 编写代码,计算'时间'和'是否堵车'的相关性
time_corr = data['时间'].corr(data['是否堵车']) 
# 编写代码,计算'污染指数'和'是否堵车'的相关性
air_corr = data['污染指数'].corr(data['是否堵车'])
# 编写代码,计算'天气'和'是否堵车'的相关性
weather_corr = data['天气'].corr(data['是否堵车'])


print('时间', time_corr)
print('污染指数', air_corr)
print('天气', weather_corr)
