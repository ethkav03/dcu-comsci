#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def tail(self):
        if self.next is None:
            return self.data
        return self.next.tail()


def reverse(node):
    if node.next is None:
        return node
    n = reverse(node.next)
    n.next = Node(node.data)
    return n

def main():
    head = Node("Dublin")
    another_node = Node("Galway")
    head.next = another_node
    a_third_node = Node("Cork")
    another_node.next = a_third_node

    print(head.data, head.tail())
    head = reverse(head)
    print(head.data, head.tail())

if __name__ == "__main__":
    main()