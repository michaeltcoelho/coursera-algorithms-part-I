from quick_union_weighted import QuickUnionWeighted


class QuickUnionPathCompression(QuickUnionWeighted):
    """Try to flatten the tree pointing all tree nodes to its root node."""

    def _root(self, i):
        while (i != self.ids[i]):
            self.ids[i] = self.ids[self.ids[i]] # path compression
            i = self.ids[i]
        return i


if __name__ == "__main__":
    quick_union_path = QuickUnionPathCompression(10)
    quick_union_path.union(2, 3)
    quick_union_path.union(1, 3)
    quick_union_path.union(3, 0)
    assert quick_union_path.connected(2, 3)
