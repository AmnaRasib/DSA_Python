vertices=['A','B','C','D']
graph=[[0]*4 for _ in range(4)]
edges=[('A','B'),('A','C'),('B','D')]

for (u,v) in edges:
    i,j= vertices.index(u),vertices.index(v)
    graph[i][j]=1
    graph[j][i]=1
print("Adjacency Matrix:")
for row in graph:
    print(row)

