
class Node:
    def __init__(self, id: int, data: dict):
        self.id = id
        self.data = data

    def __str__(self) -> str:
        ret = "id: " + str(self.id) + ", data:" + str(self.data)
        return ret
    
    def __eq__(self, other) -> bool:
        return other.data == self.data


class Edge:
    def __init__(self, id, source: Node, destination: Node):
        self.id = id
        self.source = source
        self.destination = destination

    def __str__(self) -> str:
        ret = "Edge id: " + str(self.id) + "\n"
        ret += "\t" + str(self.source) + "\n \t" + str(self.destination)
        return ret
    
    def __eq__(self, other) -> bool:
        return self.source == other.source and self.destination == other.destination


class Graph:
    def __init__(self):
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []

    def add_node(self, data: dict) -> Node:
        if len(self.nodes) != 0:
            newNode = Node(self.nodes[-1].id + 1, data)
            for node in self.nodes:
                if newNode == node:
                    return node
        else:
            newNode = Node(1, data)
        
        self.nodes.append(newNode)
        return newNode

    def add_edge(self, source: Node, destination: Node) -> Edge:
        if len(self.edges) != 0:
            newEdge = Edge(self.edges[-1].id + 1, source, destination)
            for edge in self.edges:
                if edge == newEdge:
                    return edge
        else:
            newEdge = Edge(1, source, destination)
        
        self.edges.append(newEdge)
        return newEdge
