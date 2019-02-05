from quick_union_path_compression import QuickUnionPathCompression


class LargestNumberInAComponent(QuickUnionPathCompression):

    def __init__(self, n):
        super().__init__(n)
        self.largest = list(range(n))

    def find(self, i):
        return self.largest[self._root(i)]

    def _set_largest_element(self, p_root, q_root, p, q):
        p_largest = self.largest[p_root]
        q_largest = self.largest[q_root]
        if p_largest > q_largest:
            self.largest[q_root] = p_largest
        else:
            self.largest[p_root] = q_largest

    def union(self, p, q):
        p_root = self._root(p)
        q_root = self._root(q)
        if p_root == q_root:
            return
        self._set_largest_element(p_root, q_root, p, q)
        if self.sizes[p_root] < self.sizes[q_root]:
            self.ids[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.ids[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]


if __name__ == "__main__":
    largest_number = LargestNumberInAComponent(10)
    largest_number.union(1, 2)
    largest_number.union(1, 3)
    largest_number.union(4, 5)
    largest_number.union(5, 6)
    assert largest_number.find(4) == 6
    assert largest_number.find(1) == 3
