i = [i for i in range (2,70) ]
b = [2]
for item in i :
    for i in range (len(b)):
        if b[i] == sum(b):
            print(b[i])

    for h in range(2,item):
        if item%h ==0 :
            break
        elif item%h != 0:
            b.append(item)
            break

print(b)
