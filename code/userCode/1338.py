def decisionTree(skin,vine):
    # skin是纹路, vine是瓜蔓, 可以只使用这两个参数中的一个
    # 函数的返回值是西瓜的类别
   if skin == '清晰':
       if vine == '蜷缩':
           return '能量西瓜'
        else:
            return '普通西瓜'
    else:
        if vine == '蜷缩':
            return '能量西瓜'