import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(numbers)
password = numbers[0] + numbers[1] + numbers[2]
while True:
    guess = input('请输入三位密码')
    if guess == password:
        print('密码正确')
        break
print(password)