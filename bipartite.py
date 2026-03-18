graph = {
    0:  [1, 2],
    1:  [0, 4, 3],
    2:  [0, 6, 5],
    3:  [1, 7, 13],
    4:  [1, 7, 6, 14],
    5:  [2, 8],
    6:  [2, 8, 4, 14, 12],
    7:  [3, 4, 14],
    8:  [5, 6, 9],
    9:  [8, 10, 12],
    10: [9, 11, 12],
    11: [10, 13, 15],
    12: [6, 9, 10, 14, 15],
    13: [3, 11, 15],
    14: [4, 6, 7, 12, 15],
    15: [11, 12, 13, 14]
}

color = {}

def dfs(node, current_color):
    color[node] = current_color
    for neighbor in graph[node]:
        if neighbor not in color:
            if not dfs(neighbor, 1 - current_color):
                return False
        else:
            if color[neighbor] == color[node]:
                print(f"hoyr tuilt bish . {node}-{neighbor} ijil ungutei.")
                return False
    return True

def is_bipartite(graph):
    for node in graph:
        if node not in color:         
            if not dfs(node, 0):
                return False
    return True

if is_bipartite(graph):
    group_a = [n for n, c in color.items() if c == 0]
    group_b = [n for n, c in color.items() if c == 1]
    print("hoyr tuilt mun")
    print(f"Group A: {sorted(group_a)}")
    print(f"Group B: {sorted(group_b)}")
else:
    print("hoyr tuilt bish")