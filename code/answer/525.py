import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

def df_data(season, month,  hour, temp, atemp, humidity, wind, weather):
    dict = {'季节': season, '月份': month,
            '时段': hour,  '温度': temp, '体感温度': atemp, '相对湿度': humidity, '风速': wind,'天气等级': weather, }
    df = pandas.DataFrame(dict, index=[0])
    return df


season = int(input('请输入季节:'))
month = int(input('请输入月份:'))
hour = int(input('请输入时段:'))
temp = float(input('请输入温度:'))
atemp = float(input('请输入体感温度:'))
humidity = float(input('请输入相对湿度:'))
wind = float(input('请输入风速:'))
weather = int(input('请天气等级:'))

# 加载"单车租赁数量"模型
model = joblib.load('单车租赁数量.pkl')

# 进行预测
new_data = df_data(season, month,  hour, temp, atemp, humidity, wind, weather)

y_pre = model.predict(new_data)


print('当前应该投放数量:', int(y_pre))





