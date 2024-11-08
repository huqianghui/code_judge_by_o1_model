import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
import tkinter.filedialog as tk_fld

import requests,json,io,base64

# 优化照片尺寸
def check_size(img):
    (x, y) = img.size
    if x > 350 or y > 350:
        if x > y:
            new_x = 350
            new_y = new_x / x * y
        else:
            new_y = 350
            new_x = new_y / y * x
        img = img.resize((int(new_x), int(new_y)))
    return img

# 选择照片
def select():
    global img1, pic_path
    # 读取图片路径
    pic_path = tk_fld.askopenfilename()
    if len(pic_path) != 0 :
        # 打开指定路径的图片
        img_new = Image.open(pic_path)
        img_new = check_size(img_new)
        # 替换默认图片
        img1 = ImageTk.PhotoImage(img_new)
        img_lab1.config(image=img1)


# 图片转字符串
def image_to_str(img_path):
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# 字符串转换图片
def str_to_image(b64str):
    bytes = io.BytesIO(base64.b64decode(b64str.encode('utf-8')))
    img = Image.open(bytes)
    return img

# 调取漫画服务接口
def change_pic(path):
    img_info = image_to_str(path)
    url = 'http://htapi.hetao101.com/third-proxy-service/v1/uauth/htdc_aip/selfie_anime'
    headers = {'Content-type': 'application/json'}
    img_data = json.dumps({'image': img_info, 'style': style_combo.get()})

    r = requests.post(url=url, headers=headers, data=img_data)
    r_img_data = r.json()['data']['image']
    img_new = str_to_image(r_img_data)

    return img_new

# 漫画头像
def generate():
    global pic_path, img2, img_lab2
    img_new = change_pic(pic_path)
    img2 = ImageTk.PhotoImage(img_new)
    img_lab2.config(image=img2)

# 保存图片
def save():
    global img2, file_path
    file_path = tk_fld.asksaveasfilename()
    print('你选择的路径是:', file_path)
    img2._PhotoImage__photo.write(file_path)
    print('文件已保存,去对应目录下看看吧')

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
p2 = Image.open('images/初始头像.png')
img2 = ImageTk.PhotoImage(p2)
img_lab2 = tk.Label(win, image=img2)
img_lab2.place(x=490, y=60)

# 绘制风格选择框
style_lab = tk.Label(win, text='风格:')
style_lab.place(x=530, y=350)
style_combo = ttk.Combobox(win, width=12, values=['比特莫吉', '漫威'])
style_combo.current(0)
style_combo.place(x=570, y=350)

# 绘制三个按钮
btn_select = tk.Button(win, text='选择', font=('黑体', 14), width=10, command=select)
btn_select.place(x=180, y=430)

btn_change = tk.Button(win, text='生成', font=('黑体', 14), width=10, command=generate)
btn_change.place(x=500, y=430)

btn_save = tk.Button(win, text='保存', font=('黑体', 14), width=10, command=save)
btn_save.place(x=650, y=430)

print('工具界面生成中......')

# 进入消息循环, win不断刷新
win.mainloop()