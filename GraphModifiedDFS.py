
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


def main():
    #print("hello")

    #graph_2 = read_graph_from_file('test_file')

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

    path_list = find_path(graph_1, A, D, 16)
    print(path_list)
    for v in path_list:
        print(v.id)

if __name__ == "__main__":
    main()
