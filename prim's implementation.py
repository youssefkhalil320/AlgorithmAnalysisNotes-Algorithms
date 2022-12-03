import sys
MAX_INT = sys.maxsize
v = 0

def findMinVertex(value, setMST):
  Min = MAX_INT
  vertex = 1
  for i in range(v):
    if (setMST[i] == False and value[i] < Min):
      vertex = i
      Min = value[i]
  return vertex   

def findMST(graph):
  parent = [0 for i in range(v)]
  value = [MAX_INT for i in range(v)]
  setMST = [False for i in range(v)]
  parent[0] = -1
  value[0] = 0

  for i in range(v-1):
    u = findMinVertex(value, setMST)
    setMST[u] = True
    for j in range(v):
      if graph[u][j] != 0 and setMST[j] == False and graph[u][j] < value[j] :
        value[j] = graph[u][j]
        parent[j] = u

  for l in range(v):
    print(f"U->V: {parent[l]} -> {l}  wt {graph[parent[l]][l]}")

if __name__ == '__main__':
  graph = [[0, 4, 6, 0, 0, 0],
						[4, 0, 6, 3, 4, 0],
						[6, 6, 0, 1, 8, 0],
						[0, 3, 1, 0, 2, 3],
						[0, 4, 8, 2, 0, 7],
						[0, 0, 0, 3, 7, 0] ]
  v = len(graph[0])
  findMST(graph)