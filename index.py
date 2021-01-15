from flask import Flask, render_template, request, redirect
import random
import sys

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('/index.html')

# @app.route('/algorithms/')

@app.route('/LCS/', methods=['GET', 'POST'])
def LCS():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
       
    
        var3="QabcINPUTa"+str(get_file)+".txt"
        f=open(var3,"r+")
        m=int(f.readline())
        X=f.readline()
        f.close()

        var3="QabcINPUTb"+str(get_file)+".txt"
        f=open(var3,"r+")
        n=int(f.readline())
        Y=f.readline()
        f.close()
        final=lcs(X, Y,m,n)
        print ("Length of LCS is ", final )
    
        return render_template('/LCS_result.html', res=final, val1=X, val2=Y)
       
    
    else:
        return render_template('/LCS.html')  



@app.route('/levenshtien/', methods=['GET', 'POST'])
def levenshtien():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
       
        var3="QabcINPUTa"+str(get_file)+".txt"
        f=open(var3,"r+")
        m=int(f.readline())
        X=f.readline()
        f.close()

        var3="QabcINPUTb"+str(get_file)+".txt"
        f=open(var3,"r+")
        n=int(f.readline())
        Y=f.readline()
        f.close()
        print("The Levenshtein Distance (edit-distance) is ",end = "")
        final=editDistDP(X, Y, m, n)
        print(final)
        return render_template('/leven_result.html', res=final, val1=X, val2=Y)
       
    
    else:
        return render_template('/levenshtien.html')


@app.route('/LIS/', methods=['GET', 'POST'])
def LIS():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        
        var3="QdeInput"+str(get_file)+".txt"
        arr=[]
        n=0
        f=open(var3,"r")
        n=int(f.readline())
        for i in range(n):
            arr.append(int(f.readline()))

        f.close()
        final=lis(arr)
        print("SET",get_file," LIS =",final)
        return render_template('/lis_result.html',  res=final, val1=arr)
       
    
    else:
        return render_template('/LIS.html')

   

@app.route('/MCM/', methods=['GET', 'POST'])
def MCM():
    if request.method=="POST":
        get_file=request.form.get('input')
        arr = [1, 2, 3, 4] 
        size = len(arr)
        var3="QdeInput"+str(get_file)+".txt"
        arr = []
        n = 0
        f=open(var3,"r")
        n=int(f.readline())
        for i in range(n):
            arr.append(int(f.readline()))
            
        f.close()
        final=str(MatrixChainOrder(arr, n))
        print("Minimum number of multiplications is " +	final)
        return render_template('/MCM_result.html', res=final, inp=arr)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/MCM.html')

@app.route('/knapsack/', methods=['GET', 'POST'])
def knapsack():
    if request.method=="POST":
        get_file=request.form.get('input')
        val = [] 
        wt = [] 
        W = 0
        var3="QfInput" + str(get_file) + ".txt"
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
        final=knapSack(W, wt, val, n)
        print (knapSack(W, wt, val, n))
        print(W,wt,val,n,final)
        f.close()
        return render_template('/knap_result.html', res=final,items=n, values=val,weights=wt,maxc=W)
      
    
    else:
        return render_template('/knapsack.html')


@app.route('/Partition/', methods=['GET', 'POST'])
def Partition():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        var3="QdeInput"+str(get_file)+".txt"
        arr = []
        n = 0
        f=open(var3,"r")
        n=int(f.readline())
        for i in range(n):
            arr.append(int(f.readline()))
        f.close()
        print("Set"+str(get_file),end=" ")
        if findPartition(arr, n) == True:
            print("Can be divided into two subsets of equal sum")
            possible="Can be divided into two subsets of equal sum"
            return render_template('/Partition_result.html', res=possible,inp=arr)
        else:
            possible="Can not be divided into two subsets of equal sum"
            print("Can be divided into two subsets of equal sum")
            return render_template('/Partition_result.html', res=possible,inp=arr)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/Partition.html')


@app.route('/Rod_Cutting/', methods=['GET', 'POST'])
def Rod_Cutting():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        length = None
    if request.method == "POST":
        filename = "rodcut/"
        filename = filename +"input"+ request.form.get("input")+".txt"
        f = open(filename,"r")
        count = 0

        if f.mode == 'r':
            for i in f:
                count = count + 1
            f.close()
         
        f=open(filename,"r")
        if f.mode == 'r':
            contents =f.readlines()
            val = [0 for x in range(int(count/2)+1)] 
            val[0] = 0
  
            for i in range(1, int(count/2)+1): 
                max_val = 123 
                for j in range(i): 
                    max_val = max(max_val, int(contents[j]) + val[i-j-1]) 
                    val[i] = max_val 
             
            length = val[int(count/2)]
        #code for LCS
        return render_template('/Rod_result.html', res=length)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/Rod_cutting.html')


@app.route('/Coin_Change/', methods=['GET', 'POST'])
def Coin_Change():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        length = None
        filename = "coin/"
        filename = filename +"input"+ request.form.get("input")+".txt"
         #print(filename)
        f=open(filename,"r")
        count = 0

        if f.mode == 'r':
            for i in f:
                count = count + 1
            f.close()
         
        f=open(filename,"r")
        if f.mode == 'r':
            contents =f.readlines()
            change=376
            coins = [0 for k in range(change+1)] 
            coins[0] = 1
            for i in range(0,count): 
                for j in range(int(contents[i]),change+1): 
                    coins[j] += coins[j-int(contents[i])]   
            length = coins[count]
        print(contents)
        return render_template('/Coin_result.html', res=length,ch=change)
       
    else:
        return render_template('/Coin_Change.html')


@app.route('/Word_break/', methods=['GET', 'POST'])
def Word_break():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        length = None
        filename = "word/"
        filename = filename+"input" + request.form.get("input")+".txt"
        #print(filename)
        f=open(filename,"r")
        count = 0

        if f.mode == 'r':
            for i in f:
                count = count + 1
            f.close()
         
        f=open(filename,"r")
        if f.mode == 'r':
            contents =f.readlines()
            string1="muhammadhasaan"
            if wordBreak(contents,string1):
                length = "Yes"
            else:
                length = "No"
        #code for LCS
        return render_template('/Word_result.html',inp=string1, total=contents ,res=length)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/Word_break.html')


@app.route('/SCS/',methods = ['GET','POST'])

def SCS_page():

     length = None
     if request.method == "POST":
         filename = "shortest/"
         filename = filename + "input"+ request.form.get("input")+".txt"
         #print(filename)
         f=open(filename,"r")
     
         if f.mode == 'r':
              contents =f.readlines()
              X = contents[0]
              Y = contents[1]
              a = len(X)
              b = len(Y)
              dp = [[0] * (b + 2) for i in range(a + 2)]
              for i in range(a + 1):
                 for j in range(b + 1):
                     if (not i):
                         dp[i][j] = j
                     elif (not j):
                         dp[i][j] = i
                     elif (X[i - 1] == Y[j - 1]):
                         dp[i][j] = 1 + dp[i - 1][j - 1]
                     else:
                         dp[i][j] = 1 + min(dp[i - 1][j],dp[i][j - 1])
               
              length = dp[a][b]
              print(X,Y)
         print("Length of the shortest supersequence is:",length )
         return render_template('/shortest_result.html',length=length,firs=X, sec=Y)
     else:
         return render_template('/shortes_common.html')






def lcs(X , Y, m , n): 
	 

	L = [[None]*(n+1) for i in range(m+1)] 


	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j] , L[i][j-1]) 

	return L[m][n] 


def editDistDP(str1, str2, m, n):
	# Create a table to store results of subproblems
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

	# Fill d[][] in bottom up manner
	for i in range(m + 1):
		for j in range(n + 1):

			# If first string is empty, only option is to
			# insert all characters of second string
			if i == 0:
				dp[i][j] = j # Min. operations = j

			# If second string is empty, only option is to
			# remove all characters of second string
			elif j == 0:
				dp[i][j] = i # Min. operations = i

			# If last characters are same, ignore last char
			# and recur for remaining string
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]

			# If last character are different, consider all
			# possibilities and find minimum
			else:
				dp[i][j] = 1 + min(dp[i][j-1],	 # Insert
								dp[i-1][j],	 # Remove
								dp[i-1][j-1]) # Replace

	return dp[m][n]




def lis(arr): 
	n = len(arr) 

	# Declare the list (array) for LIS and initialize LIS 
	# values for all indexes 
	lis = [1]*n 

	# Compute optimized LIS values in bottom up manner 
	for i in range (1, n): 
		for j in range(0, i): 
			if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
				lis[i] = lis[j]+1

	# Initialize maximum to 0 to get the maximum of all 
	# LIS 
	maximum = 0

	# Pick maximum of all LIS values 
	for i in range(n): 
		maximum = max(maximum, lis[i]) 

	return maximum 

def MatrixChainOrder(p, n): 
	m = [[0 for x in range(n)] for x in range(n)] 

	for i in range(1, n): 
		m[i][i] = 0

	for L in range(2, n): 
		for i in range(1, n-L + 1): 
			j = i + L-1
			m[i][j] = sys.maxsize 
			for k in range(i, j): 

				q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j] 
				if q < m[i][j]: 
					m[i][j] = q 

	return m[1][n-1] 

def findPartition(arr, n):
    sum = 0
    i, j = 0, 0
 
    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]
 
    if sum % 2 != 0:
        return False
 
    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
 
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
 
    return part[sum // 2][n]


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



def wordBreak(dict, str):
 
    if not str:
        return True
 
    for i in range(1, len(str) + 1):
 
        prefix = str[:i]
        if prefix in dict and wordBreak(dict, str[i:]):
            return True
 
    return False




if __name__ == "__main__":
    app.run(debug=True)
