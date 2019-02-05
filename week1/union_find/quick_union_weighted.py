

class QuickUnionWeighted:
    """The ideia behind this approach is to avoid tall trees, we can keep all
    trees as close as possible to its root node.
    By tracking each node size we can determine which tree is shorter and
    connect the tree being shifted to the shorter one.
    """

    def __init__(self, n):
        self.ids = list(range(n))
        self.sizes = [1] * n

    def _root(self, i):
        while (i != self.ids[i]):
            i = self.ids[i]
        return i

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        p_root = self._root(p)
        q_root = self._root(q)
        if p_root == q_root:
            return
        if self.sizes[p_root] < self.sizes[q_root]:
            self.ids[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.ids[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]


if __name__ == "__main__":
    quick_union_weighted = QuickUnionWeighted(10)
    quick_union_weighted.union(4, 3)
    quick_union_weighted.union(4, 5)
    quick_union_weighted.union(4, 6)
    assert quick_union_weighted.connected(3, 6)
