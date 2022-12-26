x = 1
y = 2
z =2
d = [1,2]

for i in range (10):
    if z!=2:
        z = x
    x = x+y
    y = z
    z +=1
    d.append(x)

print(x,y)
print(d)
