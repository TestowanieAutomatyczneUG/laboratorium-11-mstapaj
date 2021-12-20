import unittest
from src.NotesService import NotesService
from src.NotesStorage import NotesStorage
from src.Note import Note
from unittest.mock import MagicMock


class TestNotesService(unittest.TestCase):

    def setUp(self):
        self.service = NotesService()
        self.storage = NotesStorage()

    def test_NotesService_add(self):
        self.storage.add = MagicMock()
        self.storage.add.return_value = Note('Text', 4)
        self.service.notes = self.storage
        temp = Note('Text', 4)
        self.assertEqual(self.service.add(temp).note, temp.note)

    def test_NotesService_add_typeerror(self):
        self.storage.add = MagicMock()
        self.storage.add.side_effect = TypeError
        self.service.notes = self.storage
        self.assertRaises(TypeError, self.service.add, None)

    def test_averageOf_note(self):
        self.storage.getAllNotesOf = MagicMock()
        self.storage.getAllNotesOf.return_value = [Note("note", 2), Note("note", 4), Note("note", 5), Note("note", 3)]
        self.service.notes = self.storage
        self.assertEqual(self.service.averageOf('note'), 3.5)

    def test_averageOf_note_2(self):
        self.storage.getAllNotesOf = MagicMock()
        self.storage.getAllNotesOf.return_value = [Note("note", 3)]
        self.service.notes = self.storage
        self.assertEqual(self.service.averageOf('note'), 3)

    def test_averageOf_note_3(self):
        self.storage.getAllNotesOf = MagicMock()
        self.storage.getAllNotesOf.return_value = [Note("note", 2), Note("note", 4), Note("note", 5), Note("note", 2),
                                                   Note("note", 2),
                                                   Note("note", 2), Note("note", 3), Note("note", 3), Note("note", 3),
                                                   Note("note", 3)]
        self.service.notes = self.storage
        self.assertEqual(self.service.averageOf('note'), 2.9)

    def test_averageOf_zero_notes(self):
        self.storage.getAllNotesOf = MagicMock()
        self.storage.getAllNotesOf.return_value = []
        self.service.notes = self.storage
        self.assertEqual(self.service.averageOf('note'), 0)

    def test_averageOf_typeerror(self):
        self.storage.getAllNotesOf = MagicMock()
        self.storage.getAllNotesOf.side_effect = TypeError
        self.service.notes = self.storage
        self.assertRaises(TypeError, self.service.averageOf, None)

    def test_clear(self):
        self.storage.clear = MagicMock()
        self.storage.clear.return_value = 'Usunięto dane'
        self.service.notes = self.storage
        self.assertEqual(self.service.clear(), 'Usunięto dane')

    def tearDown(self):
        self.service=None
        self.storage=None
