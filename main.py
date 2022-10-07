from Graph import Graph, Vertex

if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.read().strip().split('\n')
        graph = Graph(Vertex(0, int(data[1])))
        parent_index = 0
        child_index = 1
        rows_amount = int(data[0][0])
        for line in range(1, rows_amount):
            line_data = data[line].split()
            for i in range(len(line_data)):
                lower_line_data = data[line + 1].split()
                for j in range(2):
                    graph.add_edge(parent_index=parent_index, child_index=int(child_index),
                                   value=int(lower_line_data[i + j]))
                    child_index += 1 if i == 0 and j == 0 or i == len(line_data) - 1 and j == 1 else 0.5
                parent_index += 1

    graph.print_graph()
    print()
    graph.iterate_through_graph()
    print(graph.most_experience)
