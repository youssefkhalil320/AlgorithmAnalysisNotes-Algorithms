Final = []
def printPaths(i,j,mat,dir,route = []):
    if i >= row or j >= clom:
        return 
    route.append(dir)
    if i == row-1 and j == clom-1:
        temp = route[1:]
        Final.append(temp)
    if mat[i][j] == 1:  
        printPaths(i+1,j,mat,'D')
        printPaths(i,j+1,mat,'F')
    route.pop()

 
mat = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

row = len(mat)
clom = len(mat[0])
printPaths(0,0,mat,'S')
print(Final)