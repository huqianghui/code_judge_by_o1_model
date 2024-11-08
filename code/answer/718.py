import requests
import base64, json
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog as tk_fld
# 创建窗口
win = tk.Tk()
# 设置窗口标题
win.title('文字识别')
# 设置窗口大小
win.geometry('800x500')
# 图片转base64字符串
def image_to_str(img_path):
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')
def get_words(img_path):
    # 服务接口
    url = 'http://htapi.hetao101.com/third-proxy-service/v1/uauth/handwriting'
    # 构造请求头
    headers = {'content-type': 'application/json'}
    # 构造请求体
    img_data = image_to_str(img_path)
    data = json.dumps({'image': img_data})
    # 调用接口, 发送请求
    r = requests.post(url=url, headers=headers, data=data)
    if r.status_code == 200:
        s = r.json()
        if s['errcode'] == 0:
            # 分析响应信息, 解析出文字并打印出来
            words_result = s['data']['words_result']
            words = ''
            for w in words_result:
                words += w['words']
            return words
        else:
            return '服务异常'
    else:
        return '服务异常'
# 处理图片大小(等比例缩放)
def check_size(img):
    (x, y) = img.size
    new_x = x
    new_y = y
    if x > 350 or y > 380:
        if x > y:
            new_x = 350
            new_y = new_x / x * y
        else:
            new_y = 380
            new_x = new_y / y * x
    img = img.resize((int(new_x), int(new_y)))
    return img
# 选择图片
def select():
    global img1, pic_path
    # ====编写代码, 删除文本控件中的所有内容====
    text.delete(1.0, 'end')
    # 打开选择文件窗口
    path = tk_fld.askopenfilename()
    if len(path) != 0:
        # 展示选择的图片
        pic_path = path
        img_new = Image.open(pic_path)
        img_new = check_size(img_new)
        img1 = ImageTk.PhotoImage(img_new)
        img_lab1.config(image=img1)


# 识别图片中文字,并展示在文本框中
def generate():
    global pic_path
    print('开始识别......')
    # 调用函数, 识别图片中的文字
    words = get_words(pic_path)
    # 将识别出的文字结果展示在文本控件中
    text.insert(1.0, words)

# 初始图片
pic_path = 'images/初始图片.png'

# 显示默认照片图片
p1 = Image.open(pic_path)
img1 = ImageTk.PhotoImage(p1)
img_lab1 = tk.Label(win, image=img1)
img_lab1.place(x=50, y=30)

# 显示识别结果的文本控件
text = tk.Text(win, width=48, height=26, bg='linen', borderwidth=1)
text.place(x=420, y=30)

# 选择按钮
btn_select = tk.Button(win, text='选择', font=('黑体', 14), width=10, command=select)
btn_select.place(x=160, y=430)

# 识别按钮
btn_change = tk.Button(win, text='识别', font=('黑体', 14), width=10, command=generate)
btn_change.place(x=550, y=430)

print('界面生成中......')
# 进入消息循环, win不断刷新
win.mainloop()
