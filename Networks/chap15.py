import networkx as nx

def sect_15_1(g):
    print("Start 15.1")
    g = nx.Graph()

    #add a single node3
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
    print("End 15.1")
    print()

    return g

def sect_15_2(g):
    print("Start 15.2")
    print(g.nodes())
    print(g.edges())
    print("End 15.2")
    print()

def sect_15_3(g):
    print("Start 15.3")
    #nodes are dictionaries
    print(g.nodes(data=True))
    print("End 15.3")
    

def sect_15_4(g):
    print("Start 15.4")
    g.nodes['Jeff']['job'] = 'student'
    g.nodes['Jeff']['age'] = 20
    print(g.nodes['Jeff'])
    print("End 15.4")
    print()
    return g

def sect_15_5(g):
    print("Start 15.5")
    #I'd like to be able to print items in a path
    
    lst = g.edges.data()
    for item in lst:
        print(item)
    
    print("End 15.5")
    return g
    
    
    
def main():
    g = nx.Graph()
    g = sect_15_1(g)
    sect_15_2(g)
    sect_15_3(g)
    g = sect_15_4(g)
    sect_15_5(g)


main()
