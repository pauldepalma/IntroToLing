import networkx as nx

def build_graph(g):
    g = nx.Graph()

    #add a single nod3
    g.add_node('John')
 
    #add lots of nodes
    g.add_nodes_from(['Josh', 'Jane', 'Jess', 'Jack'])

    #edge from john to jane
    g.add_edge('John', 'Jane')

    #add lots of edges
    g.add_edges_from([('Jess', 'Josh'), ('John', 'Jack'), ('Jack', 'Jane')])

    #add nodes and adges at the same time
    g.add_edges_from([('Jess', 'Jill'), ('Jill', 'Jeff'), ('Jeff', 'Jane')])

    g.remove_edge('John', 'Jane')

    g.remove_node('John')
    return g

def main():
    g = nx.Graph()

    g = build_graph(g)

    print(g.nodes())
    print(g.edges())

    #nodes are dictionaries
    print(g.nodes.data())
    g.nodes['Jeff']['job'] = 'student'
    g.nodes['Jeff']['age'] = 20
    print(g.nodes['Jeff'])

main()
