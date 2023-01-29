#!/usr/bin/env python3

class Stack:
    '''Python implementation the stack'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def postfix(stack, sum):
    for c in sum:
        if c.isdigit():
            stack.push(int(c))
        else:
            n = stack.pop()
            m = stack.pop()
            match c:
                case "+":
                    stack.push(m + n)
                case "-":
                    stack.push(m - n)
                case "*":
                    stack.push(m * n)
                case "^":
                    stack.push(m ** n)
    return stack.pop()


def main():
    s = Stack()
    print(postfix(s, "1432^*+147--+"))


if __name__ == "__main__":
    main()