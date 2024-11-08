import tkinter as tk
from tkinter import ttk
import joblib
import pandas

seasons_dict = {'春': 1, '夏': 2, '秋': 3, '冬': 4}
winds_dict = {'东北风': 1, '西北风': 2, '东南风': 3, '西南风': 4}

# 加载空气质量.pkl
model = joblib.load('空气等级.pkl')

def show():

    # 1. 取窗口数据
    season_value = seasons_dict[season_combo.get()]
    wind_value = winds_dict[wind_combo.get()]
    speed_value = speed_scale.get()
    temp_value = temp_scale.get()
    humi_value = humi_scale.get()
    pres_value = pres_scale.get()

    # 2. 使用模型来预测
    # 处理数据
    data = {}
    data['季节'] = season_value
    data['湿度'] = humi_value
    data['气压'] = pres_value
    data['温度'] = temp_value
    data['风向'] = wind_value
    data['风速'] = speed_value
    df_data = pandas.DataFrame(data, index=[0])
    # 将处理完的数据传给模型进行预测
    y_pre = model.predict(df_data)
    print('预测结果',y_pre)

# 窗体设置
win = tk.Tk()
win.geometry('600x600')
win.title('户外小助手')

# 下拉框
season_label = tk.Label(win, text='季节:')
season_label.place(x=50, y=40)
season_combo = ttk.Combobox(win, width=12, values=['春', '夏', '秋', '冬'])
season_combo.current(0)
season_combo.place(x=100, y=40)
wind_label = tk.Label(win, text='风向:')
wind_label.place(x=50, y=70)
wind_combo = ttk.Combobox(win, width=12, values=['东北风', '西北风', '东南风', '西南风'])
wind_combo.current(0)
wind_combo.place(x=100, y=70)

#  滑杆
speed_scale = tk.Scale(win, label='风速:', from_=0, to=100, orient=tk.HORIZONTAL, length=200, tickinterval=50, resolution=0.1)
speed_scale.place(x=50, y=100)
temp_scale = tk.Scale(win, label='温度:', from_=-20, to=40, orient=tk.HORIZONTAL,length=200, tickinterval=20, resolution=0.1)
temp_scale.place(x=50, y=200)
humi_scale = tk.Scale(win, label='湿度:', from_=0, to=100, orient=tk.HORIZONTAL,length=200, tickinterval=50, resolution=0.01)
humi_scale.place(x=50, y=300)
pres_scale = tk.Scale(win, label='气压:', from_=990, to=1050, orient=tk.HORIZONTAL,length=200, tickinterval=30, resolution=0.01)
pres_scale.place(x=50, y=400)

# 提交按钮
submit_button = tk.Button(win, text='提交', width=10, command=show)
submit_button.place(x=100, y=500)

# 显示天气
tip = '使用户外小助手可以得到不同天气情况下对应的空气质量,快来试试吧~'
info_label = tk.Label(win, text=tip, wraplength=270, justify='left', font=('黑体', 14))
info_label.place(x=300, y=150)

# 显示默认天气图片
img = tk.PhotoImage(file='images/初始图片.gif')
img_label = tk.Label(win, image=img)
img_label.place(x=320, y=220)

print('工具界面生成中......')

# 主循环
win.mainloop()