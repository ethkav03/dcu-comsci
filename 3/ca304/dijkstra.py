class Node:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

def shortestPath(a, f):
    pass

def main():
    f = Node("F", [])
    e = Node("E", [f])
    d = Node("D", [f])
    c = Node("C", [e, f])
    b = Node("B", [c, d])
    a = Node("A", [e, c, b])

    shortestPath(a, "F")

main()