class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def checkHeightBalanced(tree):
    if tree is None:
        return True
    return checkHeightBalanced(tree.left) and \
        checkHeightBalanced(tree.right) and \
        (get_height(tree.left) - get_height(tree.right)) <= 1

def get_height(tree):
    if tree is None:
        return 0;
    return max(get_height(tree.left), get_height(tree.right)) + 1

def print_tree(tree):
    if tree is None:
        return
    print(tree.data)
    print_tree(tree.left)
    print_tree(tree.right)

def deleteNode(tree, node):
    if tree is None or tree.left is None or tree.right is None:
        return
    if tree.left.data == node:
        tree.left = tree.left.left
        tree.right = tree.left.right
    elif tree.right.data == node:
        tree.left = tree.right.left
        tree.right = tree.right.right

    deleteNode(tree.right)
    deleteNode(tree.left)

root = Tree(1)
root.left = None
root.right = Tree(3)
root.right.left = Tree(4)
root.right.left.left = None
root.right.left.right = Tree(6)
root.right.left.right.left = Tree(7)
root.right.left.right.left.left = Tree(8)
root.right.left.right.left.left.left = None
root.right.left.right.left.left.right = Tree(10)
root.right.left.right.left.left.right.left = None
root.right.left.right.left.left.right.right = None
root.right.left.right.left.right = None
root.right.left.right.right = Tree(14)
root.right.left.right.right.left = None
root.right.left.right.right.right = None
root.right.right = None

print(checkHeightBalanced(root))
print_tree(root)
deleteNode(root, 10)
print_tree(root)