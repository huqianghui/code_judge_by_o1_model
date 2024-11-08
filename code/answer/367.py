import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ==绘制窗口及组件==
# 创建窗口
win = tk.Tk()
win.title('头像秀秀')
win.geometry('800x500')

# 绘制初始照片
p1 = Image.open('images/初始照片.png')
img1 = ImageTk.PhotoImage(p1)
img_lab1 = tk.Label(win, image=img1)
img_lab1.place(x=50, y=50)

# 绘制初始头像
# 1.使用Image的open()读取images中的'初始头像.png'
p2 = Image.open('images/初始头像.png')
# 2.使用ImageTk的PhotoImage()将p2转换成Label标签需要的图片数据
img2 = ImageTk.PhotoImage(p2)
# 3. 设置img_lab2标签的image参数
img_lab2 = tk.Label(win, image=img2)
img_lab2.place(x=490, y=60)

# 绘制风格选择框
style_lab = tk.Label(win, text='风格:')
style_lab.place(x=530, y=350)
style_combo = ttk.Combobox(win, width=12, values=['比特莫吉', '漫威'])
style_combo.current(0)
style_combo.place(x=570, y=350)

# 绘制三个按钮
btn_select = tk.Button(win, text='选择', font=('黑体', 14), width=10)
btn_select.place(x=180, y=430)

btn_change = tk.Button(win, text='生成', font=('黑体', 14), width=10)
btn_change.place(x=500, y=430)

btn_save = tk.Button(win, text='保存', font=('黑体', 14), width=10)
btn_save.place(x=650, y=430)

print('工具界面生成中......')

win.mainloop()