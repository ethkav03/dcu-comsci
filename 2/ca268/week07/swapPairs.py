#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_list(node, a):
    if len(a) == 0:
        return node
    node.next = Node(a[0])
    return build_list(node.next, a[1:])

def print_list(node):
    print(node.data)
    if node.next is None:
        return
    return print_list(node.next)

def main():
    head = [1, 2, 3, 4]
    linked = Node(head.pop(0))
    build_list(linked, head)
    print_list(linked)


if __name__ == "__main__":
    main()