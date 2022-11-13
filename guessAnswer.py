ans , guess = 37 , 0
max , min = 100 , 1
while ans != guess:
    guess = int((input(str(min)+"~"+str(max)+">> ")))
    if guess > ans:
        max = guess
        print("太大了")
    elif guess < ans:
        min = guess
        print("太小了")
print("讚啦")

import random
from random import randint as rdt
guess , ans = 0, rdt(1,100)
l , h = 0 , 100
while ans != guess:
    try:
        guess = int(input(str(l)+"~"+str(h)+">>"))
    except:
        print("請輸入正確的數字")
        continue
    if guess < l or guess > h:
        print("請輸入正確區間的數字")
        continue
    elif ans < guess:
        h = guess
        print("太大了")
    elif ans > guess:
        l = guess
        print("太小了")
    elif ans == guess:
        break
print("恭喜")
