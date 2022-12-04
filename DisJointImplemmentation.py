class DisjointSet:
    def __init__(self, vertices, parent):
        self.vertices = vertices
        self.parent = parent

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2
        
        
def main():
    vertices = ['a', 'b', 'c', 'd', 'e', 'h', 'i']
    parent = {}

    for v in vertices:
        parent[v] = v

    ds = DisjointSet(vertices, parent)
    print("Print all vertices in genesis: ")
    ds.union('b', 'd')

    ds.union('h', 'b')
    print(ds.find('h')) # prints d (OK)
    ds.union('h', 'i')
    print(ds.find('i')) # prints i (expecting d)

main()        