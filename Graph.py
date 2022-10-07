from collections import defaultdict


class Vertex:
    def __init__(self, index, value):
        self.parent = None
        self.index = index
        self.value = value
        self.current_path_experience = 0

    def visit(self):
        if self.parent:
            self.current_path_experience = self.value + self.parent.current_path_experience
        else:
            self.current_path_experience = self.value

    def __str__(self):
        return f"Vertex(index: {self.index}, " \
               f"value: {self.value}, " \
               f"current_path_experience: {self.current_path_experience}, " \
               f"parent_index: {self.parent.index if self.parent is not None else None}) "


class Graph:
    def __init__(self, root):
        self.most_experience = 0
        self.graph = defaultdict(list)
        self.vertexes = {0: root}
        self.marked = [False]

    def add_edge(self, parent_index, child_index, value):
        vertex = Vertex(child_index, value)
        self.graph[parent_index].append(vertex)
        self.vertexes.update({child_index: vertex})
        vertex.parent = self.vertexes[parent_index]
        self.marked.append(False)

    def iterate_through_graph(self):
        stack = [self.vertexes[0]]
        while len(stack) > 0:
            current_vertex = stack.pop()
            if not self.marked[current_vertex.index]:
                vertex_index = current_vertex.index
                self.marked[vertex_index] = True
                self.vertexes[vertex_index].visit()

                exp = self.vertexes[vertex_index].current_path_experience
                if exp > self.most_experience:
                    self.most_experience = exp

                for child in self.graph[vertex_index]:
                    if not self.marked[child.index]:
                        stack.append(child)

    def print_graph(self):
        for key, value in self.graph.items():
            print(
                str(key) + ": " + str([
                    f"Vertex("
                    f"index={vertex.index}, "
                    f"value={vertex.value}, "
                    f"current_path_experience={vertex.current_path_experience})"
                    for vertex in value]))
