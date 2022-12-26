i = [i for i in range (1000) ]
b = []
for item in i :
    if item%3 ==0 or item%5==0 :
        b.append(item)

print(sum(b))
