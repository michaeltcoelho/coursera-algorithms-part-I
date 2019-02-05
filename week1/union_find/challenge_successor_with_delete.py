from quick_union_path_compression import QuickUnionPathCompression


class SuccessorWithDelete(QuickUnionPathCompression):

    def __init__(self, n):
        super().__init__(n)
        self.states = [True] * n

    def find(self, i):
        pass

    def remove(self, i):
        self.states[i] = False


if __name__ == "__main__":
    successor = SuccessorWithDelete(4)
    successor.union(1, 2)
    successor.union(2, 3)
    assert successor.connected(1, 3)
    successor.remove(2)
