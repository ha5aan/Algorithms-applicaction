
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
    print("The Levenshtein Distance (edit-distance) is ",end = "")
    print(editDistDP(X, Y, m, n))
