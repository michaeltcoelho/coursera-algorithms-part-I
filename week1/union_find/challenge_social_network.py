from datetime import datetime, timedelta

from quick_union_path_compression import QuickUnionPathCompression


def get_timestamp(minutes):
    return (datetime.now() + timedelta(minutes=minutes)).time()


class Friendship:

    def __init__(self, member1, member2, timestamp):
        self.member1 = member1
        self.member2 = member2
        self.timestamp = timestamp

    def __eq__(self, friendship_a, friendship_b):
        return friendship_a.member1 == friendship_b.member1\
            and friendship_a.member2 == friendship_b.member2\
            and friendship_a.timestamp == friendship_b.timestamp


class SocialNetwork:

    def __init__(self, quick_union):
        self.quick_union = quick_union

    def load(self, friendships):
        for friendship in friendships:
            if self.quick_union._root(friendship.member1)\
                    != self.quick_union._root(friendship.member2):
                self.quick_union.union(friendship.member1, friendship.member2)

    def are_friends(self, member1, member2):
        return self.quick_union.connected(member1, member2)


if __name__ == "__main__":
    # ascending ordered tuple
    friendships = (
        Friendship(8, 10, get_timestamp(5)),
        Friendship(5, 6, get_timestamp(4)),
        Friendship(7, 0, get_timestamp(6)),
        Friendship(4, 5, get_timestamp(3)),
        Friendship(1, 3, get_timestamp(2)),
        Friendship(1, 2, get_timestamp(1)),
    )
    quick_union = QuickUnionPathCompression(11)
    social_net = SocialNetwork(quick_union)
    social_net.load(friendships)

    assert social_net.are_friends(1, 2)
    assert social_net.are_friends(4, 6)
