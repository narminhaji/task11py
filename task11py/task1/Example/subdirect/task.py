p= [1, 2, 3, 4, 5, 6, 7, 8]
s = []
for i in range(len(p)):
    s.append(1)
    for j in range(len(p)):
        if (p[j] > p[i]):
            s[i] += 1
    
print(s)