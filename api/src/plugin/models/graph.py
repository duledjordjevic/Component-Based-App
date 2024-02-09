
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
    
    def find_children(self, id: int) -> dict:
        result = {}
        
        for edge in self.edges:
            if edge.source.id == id:
                print("asd")
                key = "node_" + str(edge.destination.id)
                result[key] = {"hasChilds": "false", "id" : edge.destination.id }
                for edge2 in self.edges:
                    if edge2.source.id == edge.destination.id:
                        result[key]["hasChilds"] = "true"

        print(result)
        print(id)
        return result
    
    def find_node_which_have_children(self) -> dict:
        result = {}
        for edge in self.edges:
            key = "node_" + str(edge.source.id)
            result[key] = {"hasChilds": "true", "id" : edge.source.id }

        print(result)
        return result

    def search(self, keyword: str) -> None:
        result_nodes = []
        result_edges = []

        for node in self.nodes:
            for value in node.data.values():
                if keyword.lower() in str(value).lower():
                    result_nodes.append(node)
                    break

        for edge in self.edges:
            if edge.source in result_nodes and edge.destination in result_nodes:
                result_edges.append(edge)

        self.nodes = result_nodes
        self.edges = result_edges

    def filter(self, key, value, comparison_operator) -> bool:
        result_nodes = []
        result_edges = []

        if key not in self.nodes[0].data.keys():
            return False

        isNumber = False
        if isinstance(self.nodes[0].data[key], int):
            try:
                searchedValue = int(value)
                isNumber = True
            except:
                print("Exception")
                return False

        for node in self.nodes:
            if isNumber:
                expression = f"{node.data[key]} {comparison_operator} {value}"
            else:
                expression = f'"{node.data[key]}" {comparison_operator} "{value}"'
            print(expression)
            result = eval(expression)
            print(result)
            if result:
                result_nodes.append(node)

        for edge in self.edges:
            if edge.source in result_nodes and edge.destination in result_nodes:
                result_edges.append(edge)

        self.nodes = result_nodes
        self.edges = result_edges

        return True