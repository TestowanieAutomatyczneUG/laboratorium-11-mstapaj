import unittest
from unittest.mock import mock_open, patch, MagicMock
from src.fileEditor import fileEditor


class TestFileEditor(unittest.TestCase):
    def setUp(self):
        self.temp = fileEditor()

    def test_openFile(self):
        file = mock_open(read_data='dane z pliku\ntest')
        with file('/fake/file/path.txt', 'r') as f:
            self.assertEqual(self.temp.readFile(f), 'dane z pliku\ntest')

    def test_openFile_2(self):
        file = mock_open(read_data='123')
        with file('/fake/file/path.txt', 'r') as f:
            self.assertEqual(self.temp.readFile(f), '123')

    def test_editFile(self):
        file = mock_open(read_data='123')
        with patch("builtins.open", file):
            self.temp.editFile('/fake/file/path.txt', 'new line')
        file.assert_called_once_with('/fake/file/path.txt', 'a')

    def test_editFile_2(self):
        file = mock_open(read_data='some data')
        with patch("builtins.open", file):
            self.temp.editFile('/fake/file/path.txt', 'lineee')
        file.assert_called_once_with('/fake/file/path.txt', 'a')

    def test_editFile_none(self):
        self.assertRaises(TypeError, self.temp.editFile, None)

    def test_editFile_object(self):
        self.assertRaises(TypeError, self.temp.editFile, {})

    def test_editFile_array(self):
        self.assertRaises(TypeError, self.temp.editFile, [])

    def test_editFile_true(self):
        self.assertRaises(TypeError, self.temp.editFile, True)

    def test_editFile_false(self):
        self.assertRaises(TypeError, self.temp.editFile, False)

    def test_editFile_int(self):
        self.assertRaises(TypeError, self.temp.editFile, 3)

    def test_editFile_float(self):
        self.assertRaises(TypeError, self.temp.editFile, 2.78)

    def test_editFile_negative_int(self):
        self.assertRaises(TypeError, self.temp.editFile, -12)

    def test_editFile_negative_float(self):
        self.assertRaises(TypeError, self.temp.editFile, -2.12)

    @patch('src.fileEditor.os')
    def test_deleteFile(self, mock):
        mock.path = MagicMock()
        mock.path.exists.return_value = True
        self.temp.deleteFile('/fake/file/path.txt')
        mock.remove.assert_called_with('/fake/file/path.txt')

    @patch('src.fileEditor.os')
    def test_deleteFile_doesnt_exist(self, mock):
        mock.path = MagicMock()
        mock.path.exists.return_value = False
        self.assertRaises(Exception, self.temp.deleteFile, '/fake/file/path.txt')

    def test_deleteFile_none_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, None, 'abc')

    def test_deleteFile_none_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', None)

    def test_deleteFile_none(self):
        self.assertRaises(TypeError, self.temp.deleteFile, None, None)

    def test_deleteFile_object_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, {}, 'abc')

    def test_deleteFile_object_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', {})

    def test_deleteFile_object(self):
        self.assertRaises(TypeError, self.temp.deleteFile, {}, {})

    def test_deleteFile_array_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, [], 'abc')

    def test_deleteFile_array_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', [])

    def test_deleteFile_array(self):
        self.assertRaises(TypeError, self.temp.deleteFile, [], [])

    def test_deleteFile_true_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, True, 'abc')

    def test_deleteFile_true_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', True)

    def test_deleteFile_true(self):
        self.assertRaises(TypeError, self.temp.deleteFile, True, True)

    def test_deleteFile_false_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, False, 'abc')

    def test_deleteFile_false_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', False)

    def test_deleteFile_false(self):
        self.assertRaises(TypeError, self.temp.deleteFile, False, False)

    def test_deleteFile_int_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, 2, 'abc')

    def test_deleteFile_int_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', 4)

    def test_deleteFile_int(self):
        self.assertRaises(TypeError, self.temp.deleteFile, 3, 5)

    def test_deleteFile_float_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, 1.23, 'abc')

    def test_deleteFile_float_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', 4.12)

    def test_deleteFile_float(self):
        self.assertRaises(TypeError, self.temp.deleteFile, 2.12, 4.22)

    def test_deleteFile_negative_int_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, -3, 'abc')

    def test_deleteFile_negative_int_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', -8)

    def test_deleteFile_negative_int(self):
        self.assertRaises(TypeError, self.temp.deleteFile, -4, -6)

    def test_deleteFile_negative_float_file(self):
        self.assertRaises(TypeError, self.temp.deleteFile, -3.11, 'abc')

    def test_deleteFile_negative_float_text(self):
        self.assertRaises(TypeError, self.temp.deleteFile, '/fake/file/path.txt', -8.43)

    def test_deleteFile_negative_float(self):
        self.assertRaises(TypeError, self.temp.deleteFile, -4.12, -6.66)

    def tearDown(self):
        self.temp = None
