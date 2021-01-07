import random
from random import randint

name="18k1144"
#print("Enter Roll Number Format (18k####)")
while (len(name)<7):
    name=input()
    if(len(name)<7):
        print("Enter again")
for l in range(10):
    n=randint(10,100) #number of sets
    tt=l+1
    var3="QfInput" + str(tt) + ".txt"

    f=open(var3,"w+")
    W=name[4]+name[5]+name[6]
    f.write(W)
    f.write("\n")
    #randomlist = randint.sample(range(1, 100), n)
    #randomlist.sort()
    for i in range(n):
        w=randint(1,100)
        v=randint(1,100)
        f.write(str(w)+","+str(v))
        f.write("\n")
    #print(w,",",v)
f.close()
