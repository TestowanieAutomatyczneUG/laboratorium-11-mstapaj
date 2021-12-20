import unittest
from src.FriendShips import FriendShips


class test_FriendShips(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShips({
            "Miotk": ["Kowalski", "Nowak", "Bobkowska"],
            "Kowalski": ['Miotk'],
            "Nowak": []
        })

    def test_getFriendsList(self):
        self.assertEqual(['Miotk'], self.temp.getFriendsList('Kowalski'))

    def test_getFriendsList_2(self):
        self.assertEqual([], self.temp.getFriendsList('Nowak'))

    def test_getFriendsList_no_key(self):
        self.assertRaises(KeyError, self.temp.getFriendsList, 'Random')

    def test_getFriendsList_none(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, None)

    def test_getFriendsList_object(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, {})

    def test_getFriendsList_array(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, [])

    def test_getFriendsList_true(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, True)

    def test_getFriendsList_false(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, False)

    def test_getFriendsList_int(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, 3)

    def test_getFriendsList_float(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, 2.78)

    def test_getFriendsList_negative_int(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, -12)

    def test_getFriendsList_negative_float(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, -2.12)

    def test_areFriends(self):
        self.assertTrue(self.temp.areFriends('Kowalski', 'Miotk'))

    def test_areFriends_2(self):
        self.assertTrue(self.temp.areFriends('Miotk', 'Kowalski'))

    def test_areFriends_false(self):
        self.assertFalse(self.temp.areFriends('Nowak', 'Miotk'))

    def test_areFriends_false_2(self):
        self.assertFalse(self.temp.areFriends('Nowak', 'Kowalski'))

    def test_areFriends_no_key(self):
        self.assertRaises(KeyError, self.temp.areFriends, 'Random', 'Nowak')

    def test_areFriends_none_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, None, 'Nowak')

    def test_areFriends_none_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', None)

    def test_areFriends_none(self):
        self.assertRaises(TypeError, self.temp.areFriends, None, None)

    def test_areFriends_object_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, {}, 'Nowak')

    def test_areFriends_object_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', {})

    def test_areFriends_object(self):
        self.assertRaises(TypeError, self.temp.areFriends, {}, {})

    def test_areFriends_array_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, [], 'Nowak')

    def test_areFriends_array_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', [])

    def test_areFriends_array(self):
        self.assertRaises(TypeError, self.temp.areFriends, [], [])

    def test_areFriends_true_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, True, 'Nowak')

    def test_areFriends_true_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', True)

    def test_areFriends_true(self):
        self.assertRaises(TypeError, self.temp.areFriends, True, True)

    def test_areFriends_false_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, False, 'Nowak')

    def test_areFriends_false_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', False)

    def test_areFriends_false(self):
        self.assertRaises(TypeError, self.temp.areFriends, False, False)

    def test_areFriends_int_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, 2, 'Nowak')

    def test_areFriends_int_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', 4)

    def test_areFriends_int(self):
        self.assertRaises(TypeError, self.temp.areFriends, 3, 5)

    def test_areFriends_float_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, 1.23, 'Nowak')

    def test_areFriends_float_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', 4.12)

    def test_areFriends_float(self):
        self.assertRaises(TypeError, self.temp.areFriends, 2.12, 4.22)

    def test_areFriends_negative_int_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, -3, 'Nowak')

    def test_areFriends_negative_int_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', -8)

    def test_areFriends_negative_int(self):
        self.assertRaises(TypeError, self.temp.areFriends, -4, -6)

    def test_areFriends_negative_float_person1(self):
        self.assertRaises(TypeError, self.temp.areFriends, -3.11, 'Nowak')

    def test_areFriends_negative_float_person2(self):
        self.assertRaises(TypeError, self.temp.areFriends, 'Miotk', -8.43)

    def test_areFriends_negative_float(self):
        self.assertRaises(TypeError, self.temp.areFriends, -4.12, -6.66)

    def test_addFriend(self):
        self.assertEqual(['Nowy'], self.temp.addFriend('Nowak', 'Nowy'))

    def test_addFriend_2(self):
        self.assertEqual(["Kowalski", "Nowak", "Bobkowska", 'Nowy'], self.temp.addFriend('Miotk', 'Nowy'))

    def test_addFriend_no_key(self):
        self.assertRaises(KeyError, self.temp.addFriend, 'Random', 'Nowy')

    def test_addFriend_friends(self):
        self.assertRaises(Exception, self.temp.addFriend, 'Miotk', 'Kowalski')

    def test_addFriend_none_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, None, 'Nowak')

    def test_addFriend_none_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', None)

    def test_addFriend_none(self):
        self.assertRaises(TypeError, self.temp.addFriend, None, None)

    def test_addFriend_object_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, {}, 'Nowak')

    def test_addFriend_object_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', {})

    def test_addFriend_object(self):
        self.assertRaises(TypeError, self.temp.addFriend, {}, {})

    def test_addFriend_array_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, [], 'Nowak')

    def test_addFriend_array_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', [])

    def test_addFriend_array(self):
        self.assertRaises(TypeError, self.temp.addFriend, [], [])

    def test_addFriend_true_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, True, 'Nowak')

    def test_addFriend_true_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', True)

    def test_addFriend_true(self):
        self.assertRaises(TypeError, self.temp.addFriend, True, True)

    def test_addFriend_false_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, False, 'Nowak')

    def test_addFriend_false_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', False)

    def test_addFriend_false(self):
        self.assertRaises(TypeError, self.temp.addFriend, False, False)

    def test_addFriend_int_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, 2, 'Nowak')

    def test_addFriend_int_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', 4)

    def test_addFriend_int(self):
        self.assertRaises(TypeError, self.temp.addFriend, 3, 5)

    def test_addFriend_float_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, 1.23, 'Nowak')

    def test_addFriend_float_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', 4.12)

    def test_addFriend_float(self):
        self.assertRaises(TypeError, self.temp.addFriend, 2.12, 4.22)

    def test_addFriend_negative_int_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, -3, 'Nowak')

    def test_addFriend_negative_int_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', -8)

    def test_addFriend_negative_int(self):
        self.assertRaises(TypeError, self.temp.addFriend, -4, -6)

    def test_addFriend_negative_float_person(self):
        self.assertRaises(TypeError, self.temp.addFriend, -3.11, 'Nowak')

    def test_addFriend_negative_float_friend(self):
        self.assertRaises(TypeError, self.temp.addFriend, 'Miotk', -8.43)

    def test_addFriend_negative_float(self):
        self.assertRaises(TypeError, self.temp.addFriend, -4.12, -6.66)

    def test_makeFriends(self):
        self.assertEqual({'Kowalski': ['Miotk', 'Nowak'], 'Nowak': ['Kowalski']},
                         self.temp.makeFriends('Nowak', 'Kowalski'))

    def test_makeFriends_no_key_person1(self):
        self.assertRaises(KeyError, self.temp.makeFriends, 'Random', 'Nowak')

    def test_makeFriends_no_key_person2(self):
        self.assertRaises(KeyError, self.temp.makeFriends, 'Nowak', 'Random')

    def test_makeFriends_no_key(self):
        self.assertRaises(KeyError, self.temp.makeFriends, 'Rand', 'Random')

    def test_makeFriends_friends(self):
        self.assertRaises(Exception, self.temp.makeFriends, 'Miotk', 'Nowak')

    def test_makeFriends_friends_2(self):
        self.assertRaises(Exception, self.temp.makeFriends, 'Nowak', 'Miotk')
        
    def test_makeFriends_none_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, None, 'Nowak')

    def test_makeFriends_none_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', None)

    def test_makeFriends_none(self):
        self.assertRaises(TypeError, self.temp.makeFriends, None, None)

    def test_makeFriends_object_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, {}, 'Nowak')

    def test_makeFriends_object_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', {})

    def test_makeFriends_object(self):
        self.assertRaises(TypeError, self.temp.makeFriends, {}, {})

    def test_makeFriends_array_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, [], 'Nowak')

    def test_makeFriends_array_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', [])

    def test_makeFriends_array(self):
        self.assertRaises(TypeError, self.temp.makeFriends, [], [])

    def test_makeFriends_true_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, True, 'Nowak')

    def test_makeFriends_true_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', True)

    def test_makeFriends_true(self):
        self.assertRaises(TypeError, self.temp.makeFriends, True, True)

    def test_makeFriends_false_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, False, 'Nowak')

    def test_makeFriends_false_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', False)

    def test_makeFriends_false(self):
        self.assertRaises(TypeError, self.temp.makeFriends, False, False)

    def test_makeFriends_int_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 2, 'Nowak')

    def test_makeFriends_int_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', 4)

    def test_makeFriends_int(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 3, 5)

    def test_makeFriends_float_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 1.23, 'Nowak')

    def test_makeFriends_float_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', 4.12)

    def test_makeFriends_float(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 2.12, 4.22)

    def test_makeFriends_negative_int_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, -3, 'Nowak')

    def test_makeFriends_negative_int_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', -8)

    def test_makeFriends_negative_int(self):
        self.assertRaises(TypeError, self.temp.makeFriends, -4, -6)

    def test_makeFriends_negative_float_person1(self):
        self.assertRaises(TypeError, self.temp.makeFriends, -3.11, 'Nowak')

    def test_makeFriends_negative_float_person2(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 'Miotk', -8.43)

    def test_makeFriends_negative_float(self):
        self.assertRaises(TypeError, self.temp.makeFriends, -4.12, -6.66)
