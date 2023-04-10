from main import BooksCollector
import pytest

new_book = 'Гордость и предубеждение и зомби'
another_new_book = 'Что делать, если ваш кот хочет вас убить'
books_with_ratings = {
    new_book: 6,
    another_new_book: 10,
    '9 мест, где надо побывать с мертвой принцессой': 8
}


class TestBooksCollector:

    def test_init_books_rating_type_is_dictionary(self):
        collector = BooksCollector()

        assert collector.get_books_rating() == {}

    def test_init_favorites_type_is_list(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []

    def test_add_new_book_add_two_books_count_books_two(self):
        collector = BooksCollector()

        collector.add_new_book(new_book)
        collector.add_new_book(another_new_book)

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_two_same_books_count_books_one(self):
        collector = BooksCollector()

        collector.add_new_book(new_book)
        collector.add_new_book(new_book)

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_add_rating_to_nonexistent_book_rating_is_none(self):
        collector = BooksCollector()
        book = new_book

        collector.set_book_rating(book, 10)

        assert collector.get_book_rating(book) is None

    def test_set_book_rating_add_new_book_with_rating_less_than_one_rating_doesnt_change(self):
        collector = BooksCollector()
        book = new_book
        rating = -1

        collector.add_new_book(book)
        collector.set_book_rating(book, rating)

        assert collector.get_book_rating(book) != rating

    def test_set_book_rating_add_new_book_with_rating_more_than_ten_rating_doesnt_change(self):
        collector = BooksCollector()
        book = new_book
        rating = 15

        collector.add_new_book(book)
        collector.set_book_rating(book, rating)

        assert collector.get_book_rating(book) != rating

    def test_get_book_rating_get_nonexistent_book_rating_rating_is_none(self):
        collector = BooksCollector()

        assert collector.get_book_rating(new_book) is None

    def test_add_book_in_favorites_add_new_book_book_in_favorites(self):
        collector = BooksCollector()
        book = new_book

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert book in collector.get_list_of_favorites_books()

    def test_get_books_with_specific_rating_add_three_new_books_one_book_with_rating_more_than_eight(self):
        collector = BooksCollector()

        for book, book_rating in books_with_ratings.items():
            collector.add_new_book(book)
            collector.set_book_rating(book, book_rating)

        assert len(collector.get_books_with_specific_rating(8)) == 1

    def test_delete_book_from_favorites_add_new_book_to_favorites_count_of_books_is_zero(self):
        collector = BooksCollector()
        book = new_book

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 0
