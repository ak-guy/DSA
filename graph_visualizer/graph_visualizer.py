from graphviz import Digraph

def add_edges(graph, node):
    if node is not None:
        if node.left:
            graph.node(str(node.left.val))
            graph.edge(str(node.val), str(node.left.val))
            add_edges(graph, node.left)
        if node.right:
            graph.node(str(node.right.val))
            graph.edge(str(node.val), str(node.right.val))
            add_edges(graph, node.right)

def print_graphical_tree(root):
    dot = Digraph()
    if root:
        dot.node(str(root.val))
        add_edges(dot, root)
    dot.render('tree', format='png', cleanup=True)  # This will create a PNG file named 'tree.png'
    # dot.view('tree')  # Uncomment this line to open the file after creation

def print_graph(graph):
    dot = Digraph()
    for node, edges in graph.items():
        for edge in edges:
            dot.node(str(node))
            dot.node(str(edge))
            dot.edge(str(node), str(edge))

    dot.render('tree', format='png', cleanup=True)

g = {0: [99, 69, 3], 1: [79, 48], 2: [73], 3: [25, 65, 0], 4: [56, 84], 5: [], 6: [28, 29, 26], 7: [], 8: [], 9: [19], 10: [], 11: [82, 96], 12: [49, 27, 26], 13: [68], 14: [53], 15: [62, 79, 48], 16: [50, 85, 67, 17, 25], 17: [51, 16, 88, 86], 18: [77], 19: [69, 45, 72, 9], 20: [69, 27, 39], 21: [42, 76], 22: [41, 77], 23: [], 24: [83, 64, 27, 91], 25: [34, 88, 16, 3], 26: [12, 6, 90], 27: [20, 80, 45, 12, 24, 51, 97, 43], 28: [6], 29: [41, 72, 51, 94, 6, 81], 30: [62, 90, 69], 31: [44, 93], 32: [], 33: [83, 85, 46, 89, 95, 65, 57], 34: [25, 40, 56], 35: [90, 77, 73], 36: [], 37: [39, 48], 38: [], 39: [37, 20, 83, 98], 40: [84, 70, 42, 34], 41: [29, 64, 22, 79], 42: [56, 40, 21], 43: [27], 44: [85, 31], 45: [88, 19, 27, 56], 46: [98, 33, 47, 80], 47: [46], 48: [37, 15, 1], 49: [12], 50: [74, 16, 85], 51: [17, 29, 95, 27], 52: [61], 53: [62, 14], 54: [82], 55: [], 56: [4, 42, 65, 45, 34], 57: [58, 33], 58: [57, 92, 95], 59: [], 60: [99], 61: [52, 80, 63, 65], 62: [53, 15, 30], 63: [61, 84], 64: [41, 24, 77], 65: [56, 33, 61, 3], 66: [99, 89], 67: [71, 16, 83, 77], 68: [13], 69: [20, 79, 19, 0, 30], 70: [40, 87], 71: [67], 72: [29, 19, 96], 73: [2, 35], 74: [50], 75: [], 76: [21], 77: [35, 67, 22, 94, 64, 18], 78: [], 79: [69, 1, 41, 15, 83], 80: [27, 61, 46], 81: [29], 82: [11, 54], 83: [33, 24, 67, 39, 90, 79], 84: [40, 4, 63], 85: [44, 33, 50, 16, 90], 86: [17], 87: [70], 88: [25, 45, 17], 89: [33, 66], 90: [35, 30, 83, 85, 26], 91: [24], 92: [58], 93: [31], 94: [29, 77], 95: [51, 33, 58], 96: [11, 72], 97: [27], 98: [46, 39], 99: [60, 0, 66]}

print_graph(g)