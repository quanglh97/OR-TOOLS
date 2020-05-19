import random

f = open("Data_Schedule_Foolball.txt", "w+")
n = 10
f.write("%d\n"%(n))
d ={}
print(type(d))
for i in range(10):
    for j in range(10):
        if (j,i) in d:
            d[i, j] = d[j,i]
        else:
            d[i, j] = random.randint(1, 10)
        if(i == j):
            d[i, j] = 0
        
        f.write("%2d  "%(d[i, j]))
    f.write("\n")
f.close()