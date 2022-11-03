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
