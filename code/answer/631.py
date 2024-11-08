import tkinter as tk
import random
import os
    
all_images = os.listdir('images')
index = random.randint(0, len(all_images)-1)
cur_pic = all_images[index]

# 判断输入的成语是否正确
def judge():
    global cur_pic, tip, img
    print('开始判断...')
    # 得到玩家输入的成语及正确答案
    word = input_word.get()
    answer = cur_pic[0:4]
    # 判断玩家的输入是否正确
    if word == answer:
        # 随机获取一张成语图片
        index = random.randint(0, len(all_images)-1)
        cur_pic = all_images[index]
        # 更新成语图片
        img = tk.PhotoImage(file='images/' + cur_pic)
        img_label.config(image=img)
        # 清空输入框
        clear()
        # 更新提示信息
        tip = '猜对了! 继续猜一猜吧~'
        info_label.config(text=tip)
    else:
        # 更新提示信息
        tip = '回答错误，请重新答题'
        info_label.config(text=tip)
    print('完成判断')

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
btn_submit = tk.Button(win, text='提交', width=10, command=judge)
btn_submit.place(x=260, y=400)

# 检测电脑的tkinter版本, 如果低于8.6, 给提示
if tk.TkVersion < 8.6:
    tip = '当前使用的tkinter版本较低, 无法直接输入中文,\n 你可以先在代码区中写好成语,再粘贴进输入框'
    info_label.config(text=tip)

print('工具界面生成中...')
# 主窗口循环展示
win.mainloop()