import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = {'isbn': 33456, 'title': 'Book 1', 'author': 'Author 1'}
        self.book2 = {'isbn': 12345, 'title': 'Book 2', 'author': 'Author 2'}
        # Add setup for test books here

    # Implement test methods here
    def test_add_book(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.assertEqual(self.manager.list_books(), [self.book1, self.book2])

    def test_remove_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book(33456)
        self.assertEqual(self.manager.list_books(), [])

    def test_remove_nonexistent_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book(987)
        self.assertEqual(self.manager.list_books(), [self.book1])

if __name__ == '__main__':
    unittest.main()
