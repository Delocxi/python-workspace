list = []
for i in range(1,11):
    if i%2 ==0 :
        for j in range(1,11):
            if j%2 == 0:
                list.append(i*j)
print(list)
            
print([i*j for i in range(1,11) if i%2 == 0 for j in range(1,11) if j%2 == 0])