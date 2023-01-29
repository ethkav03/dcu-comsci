#!/usr/bin/env python3

import sys

class Node():
    def __init__(self, data, prev=None):
        self.prev = prev
        self.data = data
        self.next = None


def main():
    nums = sys.argv[1:]
    head = Node(nums[0])
    build_list(head, nums[1:])
    #print_from_head(head)
    remove_node(head, 7)
    print_from_head(head)
    print("")
    print_from_tail(head)

def build_list(lst, numbers, prev=None):
    if len(numbers) == 0:
        return
    lst.next = Node(int(numbers[0]), lst)
    return build_list(lst.next, numbers[1:], lst)

def remove_node(lst, num, prev=None):
    if lst is None:
        return
    elif lst.data == num:
        if lst.prev is not None:
            lst.prev.next = lst.next
        if lst.next is not None:
            lst.next.prev = lst.prev
        return
    return remove_node(lst.next, num, lst)














def print_from_head(lst):
    if lst is None:
        return
    print(lst.data)
    return print_from_head(lst.next)

def print_from_tail(lst):
    if lst.next is None:
        print(lst.data)
        return
    print_from_tail(lst.next)
    print(lst.data)
    return

if __name__ == "__main__":
    main()