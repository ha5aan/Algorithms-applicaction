


def shortestSuperSequence(X, Y , m , n):
	
	l = lcs(X, Y, m, n)


	return (m + n - l)




def lcs(X, Y, m, n):
	L = [[0] * (n + 2) for i in
		range(m + 2)]

	# Following steps build L[m + 1][n + 1]
	# in bottom up fashion. Note that L[i][j]
	# contains length of LCS of X[0..i - 1]
	# and Y[0..j - 1]
	for i in range(m + 1):

		for j in range(n + 1):

			if (i == 0 or j == 0):
				L[i][j] = 0

			elif (X[i - 1] == Y[j - 1]):
				L[i][j] = L[i - 1][j - 1] + 1

			else:
				L[i][j] = max(L[i - 1][j],
							L[i][j - 1])

	
	return L[m][n]


# Driver code
for i in range(10):
    tt=i+1
    var3="QabcINPUTa"+str(tt)+".txt"
    f=open(var3,"r+")
    m=int(f.readline())
    X=f.readline()
    f.close()

    var3="QabcINPUTb"+str(tt)+".txt"
    f=open(var3,"r+")
    n=int(f.readline())
    Y=f.readline()
    f.close()
    print("Length of the shortest supersequence is %d" % shortestSuperSequence(X, Y , m, n))

