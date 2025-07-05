import matplotlib.pyplot as plt
import networkx as nx

def draw_tree(adjacency_dict: dict[str, tuple[str]]):
    """Draw the Huffman tree using networkx and matplotlib."""
    H = nx.Graph(adjacency_dict)
    pos=nx.nx_pydot.graphviz_layout(H, prog='dot')
    # pos = nx.bfs_layout(H, 0, align='horizontal')
    nx.draw(H, pos=pos, arrows=True, with_labels=True)
    plt.show()