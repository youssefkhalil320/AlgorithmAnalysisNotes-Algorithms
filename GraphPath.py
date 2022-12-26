paths = []
def find_routes(grid, m, n, i, j, tempy):
    if i < 0 or i >= m or j < 0 or j >= n:
        return
    if i == m - 1 and j == n - 1:
        paths.append(tempy[:]+[9])
        return
    #grid[i][j] = '*'
    tempy.append(grid[i][j])
    find_routes(grid, m, n, i + 1, j,tempy)  # down
    find_routes(grid, m, n, i, j + 1,tempy)  # right
    find_routes(grid, m, n, i + 1, j + 1,tempy)  # down-right
    #grid[i][j] = '.'
    tempy.pop()

# Example usage
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
find_routes(grid, 3, 3, 0, 0, [])
print(paths)
