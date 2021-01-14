import random
def knapSack(W, wt, val, n):
   K = [[0 for x in range(W + 1)] for x in range(n + 1)]
   #Table in bottom up manner
   for i in range(n + 1):
      for w in range(W + 1):
         if i == 0 or w == 0:
            K[i][w] = 0
         elif wt[i-1] <= w:
            K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
         else:
            K[i][w] = K[i-1][w]
   return K[n][W]


for l in range(10):
    val = [] 
    wt = [] 
    W = 0
    tt=l+1
    var3="QfInput" + str(tt) + ".txt"
    f=open(var3,"r")
    W=int(f.readline())
    temp1=f.readline()
    while True:
        if not temp1:
            break
        tempwt = ""
        for i in range(len(temp1)-1):
            if (temp1[i]==',' ):
                wt.append(int(tempwt))
                tempwt=""
                continue
            else:
                tempwt+=temp1[i]
        val.append(int(tempwt))
        temp1=f.readline()

    n=len(val)
    print (knapSack(W, wt, val, n))
f.close()


