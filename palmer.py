def palmer(M,n,m):
	s = [0 for x in range(0,n)]
	t = [0 for x in range(0,n)]
	A = []
	l = 1
	for i in range(1,n+1):
		for j in range(1,m+1):
			s[i] = s[i]-(m-(2*j-1)) * M[i-1][j-1]

	while (l<n+1):
		maxi = max(s)
		for i in range(1,n+1):
			if maxi == s[i]:
				t[l] = i
				l += 1
				if (s[i] > 0):
					s[i] = min(s) - s[i] 
				else:
					s[i] = min(s) + s[i]
	A[0][0] = M[t[1]][1]			
	for i in range(2,m+1):
		A[1][i] = M[t[1]][1] + A[1][i-1]
	for j in range(2,n+1):
		A[j][i] = M[t[j]][1] +A[j-1][1]
		for i in range(2,m+1):
			d = max(A[j][i-1],A[j-1][i])
			A[j][i] = M[t[j],i] + d

	return A,t

		
if __name__ == '__main__':
	
	
