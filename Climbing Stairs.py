def cs(n):
    if n == 0 or n == 1:
        return n
    return cs(n-1) + cs(n-2)
for i in range(1,11):
    print(cs(i))
#lru_cahce是一個工具，它可以記住函式已經計算過的內容，並存放起來。
import functools
@functools.lru_cache(maxsize=None)
def cs(n):
    if n == 1 or n == 2:
        return n
    return cs(n-1) + cs(n-2)
for i in range(1, 11):
	print(cs(i))
# #dic做法可以不重複運算
def cs(n, dic):
    if n in dic:
        return dic[n]
    dic[n] = cs(n-1, dic) + cs(n-2, dic)
    return dic[n]
dic = {1 : 1, 2 : 2} 
for i in range(1, 11):
	print(cs(i, dic))
# #迭代做法
def cs(n):
    if n == 1 or n ==2:
        return n
    number1 = 1
    number2 = 2
    for i in range(n-2):
        number1 , number2 = number2 ,number1 + number2
    return number2
for i in range(1,11):
    print(cs(i))