import rdflib
import networkx as nx
import matplotlib.pyplot as plt
from rdflib.namespace import RDF, RDFS, OWL

# Load the ontology from the .owl file
g = rdflib.Graph()
g.parse("ontology.owl", format="xml")

# Function to create and draw class hierarchy diagram using networkx
def create_class_hierarchy():
    class_graph = nx.DiGraph()

    # Add classes to the graph
    for s, p, o in g.triples((None, RDF.type, OWL.Class)):
        class_name = s.split("#")[-1]
        class_graph.add_node(class_name)

        # If the class has a subclass
        for s2, p2, o2 in g.triples((s, RDFS.subClassOf, None)):
            subclass_name = s2.split("#")[-1]
            class_graph.add_edge(subclass_name, class_name)

    # Draw the class hierarchy
    plt.figure(figsize=(8, 6))
    nx.draw(class_graph, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
    plt.title("Class Hierarchy Diagram")
    plt.show()

# Function to create and draw object properties diagram
def create_object_properties():
    object_graph = nx.DiGraph()

    # Add object properties to the graph
    for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty)):
        prop_name = s.split("#")[-1]
        domain = g.value(s, RDFS.domain)
        range_ = g.value(s, RDFS.range)

        # Add domain and range as nodes, and property as the edge
        object_graph.add_node(domain.split("#")[-1])
        object_graph.add_node(range_.split("#")[-1])
        object_graph.add_edge(domain.split("#")[-1], range_.split("#")[-1], label=prop_name)

    # Draw the object properties diagram
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(object_graph)
    nx.draw(object_graph, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=10, font_weight="bold", arrows=True)
    edge_labels = nx.get_edge_attributes(object_graph, 'label')
    nx.draw_networkx_edge_labels(object_graph, pos, edge_labels=edge_labels)
    plt.title("Object Properties Diagram")
    plt.show()

# Function to create and draw data properties diagram
def create_data_properties():
    data_graph = nx.DiGraph()

    # Add data properties to the graph
    for s, p, o in g.triples((None, RDF.type, OWL.DatatypeProperty)):
        prop_name = s.split("#")[-1]
        domain = g.value(s, RDFS.domain)
        range_ = g.value(s, RDFS.range)

        # Add domain and range as nodes, and property as the edge
        data_graph.add_node(domain.split("#")[-1])
        data_graph.add_node(range_.split("#")[-1])
        data_graph.add_edge(domain.split("#")[-1], range_.split("#")[-1], label=prop_name)

    # Draw the data properties diagram
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(data_graph)
    nx.draw(data_graph, pos, with_labels=True, node_size=3000, node_color="lightyellow", font_size=10, font_weight="bold", arrows=True)
    edge_labels = nx.get_edge_attributes(data_graph, 'label')
    nx.draw_networkx_edge_labels(data_graph, pos, edge_labels=edge_labels)
    plt.title("Data Properties Diagram")
    plt.show()

# Generate the diagrams
create_class_hierarchy()
create_object_properties()
create_data_properties()
