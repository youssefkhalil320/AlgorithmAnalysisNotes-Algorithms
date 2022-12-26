Final = []
def printPaths(i,j,mat,route = []):
    if i >= row or j >= clom:
        return 
    route.append(mat[i][j])
    if i == row-1 and j == clom-1:
        temp = route[:]
        Final.append(temp)
    printPaths(i+1,j,mat)
    printPaths(i,j+1,mat)
    printPaths(i+1,j+1,mat)
    route.pop()

 
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = len(mat)
clom = len(mat[0])
printPaths(0,0,mat)
print(Final)