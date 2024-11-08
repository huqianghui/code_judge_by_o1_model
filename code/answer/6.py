import pandas

data = pandas.read_csv('图灵大街.csv')
data2 = data[data['时间'] <= 9]

# 计算data2中'污染指数'和'是否堵车'的相关性
air_corr = data2['污染指数'].corr(data2['是否堵车'])
# 计算data2中'天气'和'是否堵车'的相关性
weather_corr = data2['天气'].corr(data2['是否堵车'])


print('污染指数', air_corr)
print('天气', weather_corr)
