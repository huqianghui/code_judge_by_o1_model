import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(numbers)
password = numbers[0] + numbers[1] + numbers[2]

while True:
    guess = input('请输入三位密码:')
    if len(guess) !=3:
        print('输入格式错误')
        continue
    if guess == password:
        print('密码正确')
        break
    else:
        for i in range(3):
            if guess[i] == password[i]:
                print(guess[i], 'Y')
            else:
                if guess[i] in password:
                    print(guess[i], 'N')
                else:
                    print(guess[i], 'E')