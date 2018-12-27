import sys

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
                find_vertex.neighbours.append(start_vertex)

    return vertices


def getVertex(graph, vertex_id):
    try:
        vertex = next(s for s in graph if s.id == vertex_id)
        return vertex
    except:
        print("Vertex " + vertex_id + " doesn't exist in graph")
    return


def main():

    if len(sys.argv) != 5:
        print("Need 4 args: filename, z, P, K")
        return
    filename = str(sys.argv[1])
    path_value = int(sys.argv[2])
    start_vertex = str(sys.argv[3])
    end_vertex = str(sys.argv[4])

    graph_2 = read_graph_from_file(filename)
    start = getVertex(graph_2, start_vertex)
    end = getVertex(graph_2, end_vertex)

    path_list = None

    if start and end:
        path_list = find_path(graph_2, start, end, path_value)
    else:
        return

    if path_list:
        for v in path_list:
            print(v.id + "(" + str(v.value) + ")"),
            if v is not path_list[-1]:
                print('->'),

    else:
        print("Path does not exist")


if __name__ == "__main__":
    main()
