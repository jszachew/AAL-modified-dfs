
class Vertex:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.neighbours = []


def find_path(graph, start, end, saldo, path=[]):
    path = path + [start]
    saldo = saldo - start.value
    if start == end and saldo == 0:
        return path
    #if start not in graph:
    #    return None
    if saldo < 0:
        return None
    for node in start.neighbours:
        if node not in path:
            newPath = find_path(graph, node, end, saldo, path)
            if newPath:
                return newPath
    return None


def read_graph_from_file(file_name):

    with open(file_name, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    vertices = list()
    for line in lines:
        splitted_line = line.split(',')
        vertex_id = splitted_line[0]
        vertex_value = int(splitted_line[1])
        vertex = Vertex(vertex_id, vertex_value)
        vertices.append(vertex)

    for line in lines:
        splitted_line = line.split(',')
        start_vertex = next(s for s in vertices if s.id == splitted_line[0])
        for i in range(2, len(splitted_line)):
            find_vertex = next(v for v in vertices if v.id == splitted_line[i])
            if find_vertex:
                start_vertex.neighbours.append(find_vertex)

    return vertices


def main():
    #print("hello")

    graph_2 = read_graph_from_file('test_file')

    #for i in range(len(graph_2)):
    #    print(graph_2[i].id + str(graph_2[i].value))
    #    for n in graph_2[i].neighbours:
    #        print(n.id)

    vertices = list()
    A = Vertex('A', 5)
    B = Vertex('B', 3)
    C = Vertex('C', 2)
    D = Vertex('D', 6)
    E = Vertex('E', 4)
    F = Vertex('F', 2)

    A.neighbours.append(B)
    A.neighbours.append(C)
    B.neighbours.append(C)
    B.neighbours.append(D)
    C.neighbours.append(D)
    D.neighbours.append(C)
    E.neighbours.append(F)
    F.neighbours.append(C)



    graph_1= list()
    graph_1.append(A)
    graph_1.append(B)
    graph_1.append(C)
    graph_1.append(D)
    graph_1.append(E)
    graph_1.append(F)

    path_list = find_path(graph_2, A, D, 16)
    print(path_list)
    for v in path_list:
        print(v.id)

if __name__ == "__main__":
    main()
