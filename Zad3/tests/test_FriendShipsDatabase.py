import unittest
from unittest.mock import MagicMock
from src.FriendShipsDatabase import FriendShipsDatabase


class TestFriendships(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShipsDatabase()

    def test_makeFriends(self):
        self.temp.friendShips = MagicMock()
        self.temp.makeFriends("Miotk", "Kowalski")
        self.temp.friendShips.makeFriends.assert_called_with("Miotk", "Kowalski")

    def test_getFriendsList(self):
        self.temp.friendShips = MagicMock()
        self.temp.makeFriends("Miotk", "Kowalski")
        self.temp.getFriendsList("Kowalski")
        self.temp.friendShips.getFriendsList.assert_called_with("Kowalski")

    def test_getFriendsList_no_key(self):
        self.temp.friendShips = MagicMock()
        self.temp.friendShips.getFriendsList.side_effect = KeyError
        self.temp.makeFriends("Kowalski", "Nowak")
        self.assertRaises(KeyError, self.temp.getFriendsList, "Miotk")
        self.temp.friendShips.getFriendsList.assert_called_with("Miotk")

    def test_areFriends(self):
        self.temp.friendShips = MagicMock()
        self.temp.makeFriends("Miotk", "Kowalski")
        self.temp.areFriends("Kowalski", "Miotk")
        self.temp.friendShips.areFriends.assert_called_with("Kowalski", "Miotk")

    def test_areFriends_false(self):
        self.temp.friendShips = MagicMock()
        self.temp.makeFriends("Miotk", "Kowalski")
        self.temp.makeFriends("Miotk", "Nowak")
        self.temp.areFriends("Kowalski", "Miotk")
        self.temp.friendShips.areFriends.assert_called_with("Kowalski", "Miotk")

    def test_areFriends_no_key(self):
        self.temp.friendShips = MagicMock()
        self.temp.friendShips.areFriends.side_effect = KeyError
        self.temp.makeFriends("Miotk", "Kowalski")
        self.assertRaises(KeyError, self.temp.areFriends, "Random", "Kowalski")
        self.temp.friendShips.areFriends.assert_called_with("Random", "Kowalski")
