from src.FriendShips import FriendShips


class FriendShipsDatabase:
    def __init__(self, friends=None):
        if friends is None:
            friends = {}
        self.friendShips = FriendShips(friends)

    def makeFriends(self, person1, person2):
        self.friendShips.makeFriends(person1, person2)

    def getFriendsList(self, person):
        self.friendShips.getFriendsList(person)

    def areFriends(self, person1, person2):
        self.friendShips.areFriends(person1, person2)

    def addFriend(self, person, friend):
        self.friendShips.addFriend(person, friend)
