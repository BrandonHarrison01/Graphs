from util import Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices = {}
  
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        graph.add_edges(pair[1], pair[0])

    queue = Queue()
    queue.enqueue([starting_node])
    max_path_length = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        path = queue.dequeue()
        v = path[-1]

    if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
        earliest_ancestor = v
        max_path_length = len(path)

    for neighbor in graph.vertices[v]:
        path_copy = list(path)
        path_copy.append(neighbor)
        queue.enqueue(path_copy)

    return earliest_ancestor