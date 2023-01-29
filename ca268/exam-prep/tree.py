class Tree():
    class newNode:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None

    def insertLevelOrder(self, arr, i, n):
        root = None
        if i < n:
            root = self.newNode(arr[i])
            root.left = self.insertLevelOrder(arr, 2 * i + 1, n)
            root.right = self.insertLevelOrder(arr, 2 * i + 2, n)
        return root

    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    def preOrder(self, root):
        if root is None:
            return;
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" ")

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = Tree()
    n = len(arr)
    root = None
    root = t.insertLevelOrder(arr, 0, n)
    t.inOrder(root)
    print("")
    t.preOrder(root)
    print("")
    t.postOrder(root)