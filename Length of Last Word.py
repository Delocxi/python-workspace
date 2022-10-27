s = "   fly me   to   the moon  "
A = s.split(" ")
for i in range(len(s)):
    if "" in A:
        A.remove("")
print(A) 