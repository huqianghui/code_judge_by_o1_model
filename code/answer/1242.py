import tkinter as tk
import random
import os

all_images = os.listdir('images')
# 编写代码, 在游戏开始的时候, 随机展示一张图片
index = random.randint(0, len(all_images)-1)
cur_pic = all_images[index] 


def clear():
    input_word.delete(0, 'end')


# 定义一个主窗口
win = tk.Tk()
# 窗口宽高为500
win.geometry('500x500')
# 窗口的标题
win.title('成语猜猜猜')

# 显示成语图片
img = tk.PhotoImage(file='images/' + cur_pic)
img_label = tk.Label(win, image=img)
img_label.place(x=100, y=50)

# 答案输入框
input_word = tk.Entry(win, width=25)
input_word.place(x=180, y=300)

# 提示信息
tip = '图中描述的是哪个成语'
info_label = tk.Label(win, text=tip, justify='center', font=('黑体', 12))
info_label.place(x=185, y=340)


# 清空按钮
btn_clean = tk.Button(win, text='清空', width=10, command=clear)
btn_clean.place(x=160, y=400)

# 提交按钮
btn_submit = tk.Button(win, text='提交', width=10)
btn_submit.place(x=260, y=400)


print('工具界面生成中...')
# 主窗口循环展示
win.mainloop()
