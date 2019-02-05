

class QuickUnion:

    def __init__(self, n):
        self.ids = list(range(n))

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
        self.ids[p_root] = q_root


if __name__ == "__main__":
    quick_union = QuickUnion(10)
    quick_union.union(4, 3)
    quick_union.union(4, 5)
    quick_union.union(4, 6)
    assert quick_union.connected(3, 6)
