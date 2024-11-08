import tkinter as tk

win = tk.Tk()
win.geometry('600x600')
win.title('企鹅分类')

culmen_length_label = tk.Label(win, text='喙的长度(mm)')
culmen_length_label.pack()
culmen_length_entry = tk.Entry(win, width=10)
culmen_length_entry.pack()

culmen_depth_label = tk.Label(win, text='喙的厚度(mm)')
culmen_depth_label.pack()
culmen_depth_entry = tk.Entry(win, width=10)
culmen_depth_entry.pack()

flipper_length_label = tk.Label(win, text='鳍的长度(mm)')
flipper_length_label.pack()
flipper_length_entry = tk.Entry(win, width=10)
flipper_length_entry.pack()

body_mass_label = tk.Label(win, text='体重(g)')
body_mass_label.pack()
body_mass_entry = tk.Entry(win, width=10)
body_mass_entry.pack()

gender_label = tk.Label(win, text='性别(雌性输入1, 雄性输入2)')
gender_label.pack()
gender_entry = tk.Entry(win, width=10)
gender_entry.pack()

card = tk.PhotoImage(file='德雷.gif')
img = tk.Label(win, image=card)
img.pack()

# ==========在下面编写代码==========
# 获取用户输入的5个特征数据
def show():
    global culmen_length, culmen_depth, flipper_length, body_mass, gender
    culmen_length = float(culmen_length_entry.get())
    culmen_depth = float(culmen_depth_entry.get())
    flipper_length = float(flipper_length_entry.get())
    body_mass = float(body_mass_entry.get())
    gender = float(gender_entry.get())
    print(culmen_length, culmen_depth, flipper_length, body_mass, gender)


submit_button = tk.Button(win, text='提交数据', command=show)
submit_button.pack()

print('请到电脑桌面查看小程序, 并在30秒内完成测试')
win.mainloop()








