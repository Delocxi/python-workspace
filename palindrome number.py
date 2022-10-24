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