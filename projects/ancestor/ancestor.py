
def earliest_ancestor(ancestors, starting_node):
    stack = []
    visited = set()
    max_list = []
    
    stack.append([starting_node])

    while len(stack) > 0:
        path = stack.pop()
        v = path[-1]

        print(path, 'path', v, 'v', stack, 'stack')

        if v not in visited:
            visited.add(v)

            for neighbors in ancestors:
                # print(neighbors[1])
                if v == neighbors[1]:
                    # print([*path, neighbors[0]])
                    current = [*path, neighbors[0]]

                    if len(current) > len(max_list):
                        max_list = [*current]

                    if len(current) == len(max_list):
                        if current[-1] < max_list[-1]:
                            max_list = [*current]

                    stack.append(current)

    if len(max_list) == 0:
        return -1

    return max_list[-1]


test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test, 7))


