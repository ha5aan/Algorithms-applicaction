'''# Function to find the most efficient way to multiply
# given sequence of matrices
def MatrixChainMultiplication(arr, i, j):
 
    # base case: one matrix
    if j <= i + 1:
        return 0
 
    # stores minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i+1]...M[j] = M[i..j]
    min = float('inf')
 
    # take the minimum over each possible position at which the
    # sequence of matrices can be split
 
    """
        (M[i+1]) x (M[i+2]..................M[j])
        (M[i+1]M[i+2]) x (M[i+3.............M[j])
        ...
        ...
        (M[i+1]M[i+2]............M[j-1]) x (M[j])
    """
 
    for k in range(i + 1, j):
 
        # recur for M[i+1]..M[k] to get an i x k matrix
        cost = MatrixChainMultiplication(arr, i, k)
 
        # recur for M[k+1]..M[j] to get a k x j matrix
        cost += MatrixChainMultiplication(arr, k, j)
 
        # cost to multiply two (i x k) and (k x j) matrix
        cost += arr[i] * arr[k] * arr[j]
 
        if cost < min:
            min = cost
 
    # return min cost to multiply M[j+1]..M[j]
    return min

for l in range(10):
	tt=l+1
	var3="QdeInput"+str(tt)+".txt"
	arr = []
	n = 0
	f=open(var3,"r")
	n=int(f.readline())
	for i in range(n):
		arr.append(int(f.readline()))

	f.close(),print("Minimum cost is", MatrixChainMultiplication(arr, 0, n - 1))'''
# Dynamic Programming Python implementation of Matrix 
# Chain Multiplication. See the Cormen book for details 
# of the following algorithm 
import sys 

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n 
def MatrixChainOrder(p, n): 
	# For simplicity of the program, one extra row and one 
	# extra column are allocated in m[][]. 0th row and 0th 
	# column of m[][] are not used 
	m = [[0 for x in range(n)] for x in range(n)] 

	# m[i, j] = Minimum number of scalar multiplications needed 
	# to compute the matrix A[i]A[i + 1]...A[j] = A[i..j] where 
	# dimension of A[i] is p[i-1] x p[i] 

	# cost is zero when multiplying one matrix. 
	for i in range(1, n): 
		m[i][i] = 0

	# L is chain length. 
	for L in range(2, n): 
		for i in range(1, n-L + 1): 
			j = i + L-1
			m[i][j] = sys.maxsize 
			for k in range(i, j): 

				# q = cost / scalar multiplications 
				q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j] 
				if q < m[i][j]: 
					m[i][j] = q 

	return m[1][n-1] 

# Driver program to test above function 
arr = [1, 2, 3, 4] 
size = len(arr) 
for l in range(10):
	tt=l+1
	var3="QdeInput"+str(tt)+".txt"
	arr = []
	n = 0
	f=open(var3,"r")
	n=int(f.readline())
	for i in range(n):
		arr.append(int(f.readline()))

	f.close(), print("Minimum number of multiplications is " +	str(MatrixChainOrder(arr, n))) 
# This Code is contributed by Bhavya Jain 
