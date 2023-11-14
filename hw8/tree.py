class Tree:
    """
    Simple class for representing trees.

    Public attributes:
        node_id [Any]: a unique identifier for the tree node
        val [Any]: the value associated with a node
        children [List[Tree]]: the node's children
    
    Public methods:
        add_child: adds a child to the tree
        print_tree: prints the tree
    """

    def __init__(self, node_id, val):
        self.node_id = node_id
        self.val = val
        self.children = []
        
    def add_child(self, child):
        """
        Add a child to the tree:

        Inputs:
            child [Tree]: the tree to add
        """
        assert isinstance(child, Tree)
        
        self.children.append(child)

    def print_tree(self, tabs=""):
        """
        Print the tree.

        Inputs:
            tabs [str]: a string of spaces to use for indentation 
        """
        print(tabs + f"Node {self.node_id}: {self.val}")
        for kid in self.children:
            kid.print_tree(tabs + "  ")


def load_tree(filename):
    '''
    Loads the tree from a file.

    Inputs:
      filename [str]: The name of the file to load the tree from.

    Returns [Tree]: The root of the tree or ``None`` if the file does
      not exist.
    '''
    try:
        with open(filename) as test_file:
            input_lines = test_file.read().strip().split('\n')
    except OSError:
        return None

    num_nodes = int(input_lines[0])
    # Create the nodes
    nodes = {}
    for line in input_lines[1:num_nodes + 1]:
        node_id, value = line.split()
        nodes[int(node_id)] = Tree(int(node_id), int(value))

    # Build the tree
    for line in input_lines[num_nodes + 1:]:
        parent, child = line.split()
        nodes[int(parent)].add_child(nodes[int(child)])

    return nodes[1]

