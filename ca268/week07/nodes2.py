class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def find(self, rslt):
        if self.data == rslt:
            return self
        return self.next.find(rslt)


def main():
    head = Node("Dublin")
    another_node = Node("Galway")
    head.next = another_node
    a_third_node = Node("Cork")
    another_node.next = a_third_node

    result = head.find("Galway")
    print(result.data) # Galway


if __name__ == "__main__":
    main()