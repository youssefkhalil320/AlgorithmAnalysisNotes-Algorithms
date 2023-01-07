p = [0,1,2,5,6]
wt = [0,2,3,4,5]
m = 8 
n = 4
mem = [[-1 for j in range(m+1)]for i in range(len(p))]
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            mem[i][j]  = 0
        elif wt[i] <= j:
            mem[i][j] = max(p[i]+mem[i-1][j-wt[i]] , mem[i-1][j]) 
        else:
            mem[i][j] = mem[i-1][j]
            
print(mem[n][m])
            
            
