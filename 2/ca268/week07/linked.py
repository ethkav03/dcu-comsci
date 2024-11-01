class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None

def build_list(node, n=1):
    if n == 51:
        return node
    node.next = Node(n * 2)
    return build_list(node.next, n + 1)

def print_list(node):
    print(node.data)
    if node.next is None:
        return
    return print_list(node.next)

def main():
    head = Node(0)
    build_list(head)
    print_list(head)


if __name__ == "__main__":
    main()