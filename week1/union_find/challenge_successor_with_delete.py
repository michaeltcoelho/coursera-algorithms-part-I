from challenge_largest_number import LargestNumberInAComponent


class SuccessorWithDelete(LargestNumberInAComponent):

    def __init__(self, n):
        super().__init__(n)
        self.deleted = [False] * n

    def successor(self, i):
        if not self.deleted[i]:
            return i
        else:
            return self.find(i)

    def remove(self, i):
        i_state = self.deleted[i] = True
        if i_state and not self.deleted[i + 1]:
            self.union(i, i + 1)
        if i_state and not self.deleted[i - 1]:
            self.union(i, i - 1)


if __name__ == "__main__":
    successor_with_delete = SuccessorWithDelete(4)
    successor_with_delete.remove(2)
    assert successor_with_delete.successor(2) == 3
    successor_with_delete.remove(1)
    assert successor_with_delete.successor(1) == 3
