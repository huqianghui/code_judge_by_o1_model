import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry('600x600')
win.title('户外小助手')

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



# 绘制风速的滑杆
speed_scale = tk.Scale(win, label="风速：", from_=0, to=100, orient=tk.HORIZONTAL)
speed_scale.place(x=50, y=100)


print('工具界面生成中......')
win.mainloop()