from random import randint
n=randint(30,100)
for i in range(10):
    tt=i+1
    var3="QdeInput" + str(tt) + ".txt"

    f=open(var3,"w+")
    f.write(str(n))#total inputs
    f.write("\n")
    for j in range(n):#inputs generated
        var1=randint(0,100)
        f.write(str(var1))
        f.write("\n")
    f.close()
