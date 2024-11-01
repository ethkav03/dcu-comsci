class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def reverse(self):
        return self.items[::-1]

    def sort(self, i=0):
        if len(self.items) - 1 > i:
            min = i
            for n in range(i, len(self.items)):
                if self.items[n] < self.items[min]:
                    min = n
            num = self.items[min]
            self.items.pop(min)
            self.items.insert(i, num)
            return self.sort(i + 1)

    def reversek(self, k):
        return (self.items[:k])[::-1] + self.items[k:]

    def binary(self, n):
        a = []
        for i in range(1, n + 1):
            a.append(format(i, 'b'))

        return " ".join(a)

    def asterisks(self, s):
        a = []
        b = []
        for c in s:
            if c.isalpha():
                a.append(c)
            elif c == '*':
                b.append(a.pop())
        return b

    def asterisks(self, s):
        a = []
        for c in s:
            if c.isalpha():
                a.append(c)
        return a
                


if __name__ == '__main__':
    q = Queue()
    q.enqueue(6)
    q.enqueue(1)
    q.enqueue(9)
    q.enqueue(8)
    q.enqueue(2)
    q.enqueue(7)
    q.enqueue(56)
    q.enqueue(93)
    q.enqueue(5)
    q.enqueue(11)
    q.enqueue(3)
    q.enqueue(99)
    #print(q.dequeue())
    #print(q.size())
    #print(q.dequeue())
    #print(q.dequeue())
    #print(q.is_empty())
    #print(q.size())
    print(q.items)
    #print(q.reverse())
    #print(q.reversek(2))
    q.sort()
    print(q.items)
    #print(q.binary(16))
    #print(q.asterisks("EAS*Y*QUE***ST***IO*N***"))