from PIL import Image

# 打开图片 '藏宝图.png' 和 '碎片5.png'
bg = Image.open('藏宝图.png')
im = Image.open('碎片5.png')

# 翻转图片 im
im =im.transpose(0)

# 在图片 bg 上粘贴图片 im
bg.paste(300,300)

# 保存并展示图片
bg.save('藏宝图.png')
print('图片展示中...')
bg.show()