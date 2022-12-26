# I used the solution of Geeks for Geeks 
class Graph:
    # Allocates memory for adjacency list
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
   
    # Returns true if graph has path more than k length
    def pathMoreThanK(self,src, k):
        # Create a path array with nothing included
        # in path
        path = [False]*self.V
       
        # Add source vertex to path
        path[src] = 1
       
        return self.pathMoreThanKUtil(src, k, path)
       
    # Prints shortest paths from src to all other vertices
    def pathMoreThanKUtil(self,src, k, path):
        # If k is 0 or negative, return true
        if (k <= 0):
            return True
       
        # Get all adjacent vertices of source vertex src and
        # recursively explore all paths from src.
        i = 0
        while i != len(self.adj[src]):
            # Get adjacent vertex and weight of edge
            v = self.adj[src][i][0]
            w = self.adj[src][i][1]
            i += 1
       
            # If vertex v is already there in path, then
            # there is a cycle (we ignore this edge)
            if (path[v] == True):
                continue
       
            # If weight of is more than k, return true
            if (w >= k):
                return True
       
            # Else add this vertex to path
            path[v] = True
       
            # If this adjacent can provide a path longer
            # than k, return true.
            if (self.pathMoreThanKUtil(v, k-w, path)):
                return True
       
            # Backtrack
            path[v] = False
       
        # If no adjacent could produce longer path, return
        # false
        return False
      
    # Utility function to an edge (u, v) of weight w
    def addEdge(self,u, v, w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])
# Create a graph given in the above diagram
g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 0, 4)
g.addEdge(1, 7, 11)
g.addEdge(2, 1, 8)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 2, 7)
g.addEdge(3, 5, 14)
g.addEdge(3, 4, 9)
g.addEdge(4, 3, 9)
g.addEdge(4, 5, 10)
g.addEdge(5, 3, 14)
g.addEdge(5, 2, 4)
g.addEdge(5, 4, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 5, 2)
g.addEdge(6, 8, 6)
g.addEdge(6, 7, 1)
g.addEdge(7, 6, 1)
g.addEdge(7, 8, 7)
g.addEdge(7, 1, 11)
g.addEdge(7, 0, 8)
g.addEdge(8, 2, 2)
g.addEdge(8, 7, 7)
g.addEdge(8, 6, 6)
print("YES") if g.pathMoreThanK(0, 62) else print("NO")
 
