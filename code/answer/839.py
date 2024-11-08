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

def show():
    print('按钮被点击了!')

submit_button = tk.Button(win, text="提交数据", command=show)
submit_button.pack()

print('请到电脑桌面查看小程序')
win.mainloop()
