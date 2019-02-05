
class QuickFind:

    def __init__(self, n):
        self.ids = list(range(n))

    def connected(self, p, q):
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        pid = self.ids[p]
        qid = self.ids[q]
        for _id in self.ids:
            if self.ids[_id] == pid:
                self.ids[_id] = qid


if __name__ == "__main__":
    quick_find = QuickFind(10)
    quick_find.union(4, 3)
    assert quick_find.connected(4, 3)
