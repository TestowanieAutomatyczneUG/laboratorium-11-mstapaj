def isString(word):
    if isinstance(word, str):
        return True
    else:
        raise TypeError('Tekst musi być typu string')


class FriendShips:
    def __init__(self, friendships=None):
        if friendships is None:
            friendships = {}
        if isinstance(friendships, dict):
            self.friendships = friendships
        else:
            raise TypeError('Argument musi być słownikiem')

    def makeFriends(self, person1, person2):
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)
        return {person1: self.friendships[person1], person2: self.friendships[person2]}

    def getFriendsList(self, person):
        if isString(person):
            if person in self.friendships.keys():
                return self.friendships[person]
            else:
                raise KeyError('Brak takiej osoby')

    def areFriends(self, person1, person2):
        if isString(person1) and isString(person2):
            if person1 in self.friendships.keys():
                return person2 in self.friendships[person1]
            else:
                raise KeyError('Brak takiej osoby')

    def addFriend(self, person, friend):
        if isString(person) and isString(friend):
            if person in self.friendships.keys():
                if not self.areFriends(person, friend):
                    self.friendships[person].append(friend)
                    return self.friendships[person]
                else:
                    raise Exception('Te osoby już są przyjaciółmi')
            else:
                raise KeyError('Brak takiej osoby')
