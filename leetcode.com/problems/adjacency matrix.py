import random

# [1,0,1]
# [0,1,1]
# [0,0,1]

# vertices [(0,1), (1,0), (2,0), (2,1)]


# Expected False
arr1 = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]

# Expected False
arr2 = [[0, 0, 0], [1, 0, 1], [0, 1, 1]]

# Expected True
arr3 = [[0, 1, 1], [0, 1, 1], [1, 1, 1]]

arr4 = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]


class Vertex():

    def __init__(self, id, row, column):
        self.id = id  # id of a vertex (starts at 0)
        self.count = 0  # a count that we use to determine at the very end if we have went through all the vertices that have the value of 0 in the matrix
        self.adj = []  # adjacent vertices
        self.row = row  # row value of the vertex
        self.column = column  # column value of the vertex
        self.visited = False  #

    def createEdge(self, adjVertex):
        self.adj.append(adjVertex)
        adjVertex.adj.append(self)


def createEdges(vertices):
    # Create our edges
    for vertex in vertices:
        for adj in vertices:
            if vertex == adj:
                continue
            if abs(vertex.row - adj.row == 1) and vertex.column == adj.column:
                vertex.createEdge(adj)

            elif abs(vertex.column - adj.column == 1) and vertex.row == adj.row:
                vertex.createEdge(adj)

    return vertices


def createVertices(arr):
    vertices = []

    # Create a vertex everytime a '0' is encountered
    vertexID = 0
    for row in range(len(arr)):
        for column in range(len(arr)):
            if arr[row][column] == 0:
                vertices.append(Vertex(vertexID, row, column))
                vertexID += 1

    return vertices


def reachable(arr):
    vertices = createEdges(createVertices(arr))
    #    for vertex in vertices:
    #        print("Vertex #", vertex.id)
    #        for adj in vertex.adj:
    #            print("   Has an edge to Vertex #", adj.id)

    visitedCount = BFS(vertices)

    return visitedCount == len(vertices)


def BFS(vertices):
    for vertex in vertices:
        vertex.visited = False

    queue = []
    randIndex = random.randint(0, len(vertices) - 1)
    startVertex = vertices[randIndex]
    queue.append(startVertex)

    while queue:
        popper = queue.pop(0)
        popper.visited = True
        startVertex.count += 1

        for i in popper.adj:
            if i.visited == False:
                queue.append(i)

    return startVertex.count


print(reachable(arr4))







