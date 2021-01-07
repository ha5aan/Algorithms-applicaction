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
        print(get_file)
        #code for LCS
        return render_template('/MCM_result.html', res=get_file)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/MCM.html')

@app.route('/knapsack/', methods=['GET', 'POST'])
def knapsack():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        #code for LCS
        return render_template('/knap_result.html', res=get_file)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/knapsack.html')


@app.route('/Partition/', methods=['GET', 'POST'])
def Partition():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        #code for LCS
        return render_template('/Partition_result.html', res=get_file)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/Partition.html')


@app.route('/Rod_Cutting/', methods=['GET', 'POST'])
def Rod_Cutting():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        #code for LCS
        return render_template('/Rod_result.html', res=get_file)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/Rod_cutting.html')


@app.route('/Coin_Change/', methods=['GET', 'POST'])
def Coin_Change():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        #code for LCS
        return render_template('/Coin_result.html', res=get_file)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/Coin_Change.html')


@app.route('/Word_break/', methods=['GET', 'POST'])
def Word_break():
    if request.method=="POST":
        get_file=request.form.get('input')
        print(get_file)
        #code for LCS
        return render_template('/Word_result.html', res=get_file)
       # return render_template('/output_lcs.html', res=result_LCS)
    
    else:
        return render_template('/Word_break.html')



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



if __name__ == "__main__":
    app.run(debug=True)
