x = input()
y = str(x)
z = len(y)
if z == 1:
    print("True")
else:
    for i in range(int(z/2)):
            if y[i] == y[-i-1]:
                i = i+1
                if i == int(z/2):
                    print("True")
            else:
                print("False")
                break

Arr = input()
flag = 0
A = len(Arr)
for i in range(A):
    if Arr[i] == Arr[A-1-i]:
        if i >= A-i:
             break   
    else:
        flag = 1
if flag == 0:
    print("yes")
else:
    print("no")