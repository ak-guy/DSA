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

