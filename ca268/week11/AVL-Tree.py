from libs.tree_map import TreeMap


class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree."""

    # ---------------- nested _Node class --------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing."""
        __slots__ = '_height'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0  # will be recomputed during balancing

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

    # --------------- positional-based utility methods --------------------
    def _recompute_height(self, p):
        if self is None:
            return 0;
        return max(self._recompute_height(p), self._recompute_height(p))

    def _isbalanced(self, p):
        if self is None:
            return True
        return self._isbalanced(self.left) and \
            self._isbalanced(self.right) and \
            (self._recompute_height(self.left) - self._recompute_height(self.right)) <= 1

    def _tall_child(self, p, favorleft=False):
        # if two children have same heights, decision depends on the favorleft Boolean value.
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced(p):
                # perform trinode restructuing, setting p to resulting root,
                # and recompute new local heights after the restructuing
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)

    # ------------------ override balancing hooks ------------------------------
    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)


# construct the AVL tree
avl = AVLTreeMap()
input = [84, 13, 33, 91, 19, 16, 96, 26, 34]

for i, n in enumerate(input):
    avl[n] = n

print(avl.__str__())

