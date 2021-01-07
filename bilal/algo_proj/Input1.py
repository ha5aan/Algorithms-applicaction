from random import randint
#var1 = "Bilal"
def remove(string): 
    return string.replace(" ", "")
var1=input()
var1=var1.replace(" ", "")
var1=var1.upper()
v=len(var1)
for j in range(10):
    n=randint(30,100)
    tt=j+1
    var3="QabcINPUTa" + str(tt)  + ".txt"

    f=open(var3,"w+")
    f.write(str(n))#total inputs
    f.write("\n")
    for i in range(n):
    
        va2=randint(0,v-1)
        f.write(var1[va2])
    f.write("")
    f.close()

var1=input()
var1=var1.replace(" ", "")
var1=var1.upper()
v=len(var1)
for j in range(10):
    n=randint(30,100)
    tt=j+1
    var3="QabcINPUTb" + str(tt)  + ".txt"

    f=open(var3,"w+")
    f.write(str(n))#total inputs
    f.write("\n")
    for i in range(n):
    
        va2=randint(0,v-1)
        f.write(var1[va2])
    f.write("")
    f.close()
