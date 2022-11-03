n = int(input())
Arr = []
i = 2
print(n,"=",end="")
if n == 2:
    print(n,"= 1 *",n)
else:
    while True:
        if n%i == 0:
            Arr.append(i)
            n = n / i
            if n == 1:
                break  
        elif n%i != 0 :
            i += 1
            if i == n:
                Arr.append(i)
                break
    if len(Arr) == 1:
        print("1*",n)
    else:
        L = len(Arr)
        cnt = 0
        for i in Arr:
            cnt += 1
            if cnt != L:
                print ( i,end="*")
            else:
                print ( i,end=" ")