from PIL import Image

# 打开图片 '藏宝图.png' 和 '碎片3.png'
bg = Image.open('藏宝图.png')
im = Image.open('碎片3.png')

# 裁剪图片 im
im = im.crop((50, 50, 350, 350))

# 在图片 bg 上粘贴图片 im
bg.paste(im,(600,0))

# 保存并展示图片
bg.save('藏宝图.png')
print('图片展示中...')
bg.show()

