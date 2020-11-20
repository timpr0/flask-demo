from app.main import db
from app.main.model.book import Book
from ..utils.dto import BookDao
from ..service.author_service import get_author_by_id


def get_all_books() -> [Book] or None:
    return Book.query.all()


def get_book_by_isbn(isbn: int) -> Book:
    return Book.query.filter_by(isbn=isbn).first()


def save_book(dao: BookDao) -> None:
    db.session.add(dao)
    db.session.commit()


def update_book(isbn: int, data):
    try:
        book = get_book_by_isbn(isbn)
        if not book:
            return {"message": "Das Buch wurde nicht gefunden"}, 404

        book.isbn = data['isbn']
        book.title = data['title']
        book.description = data['description']
        book.author_id = data['author_id']
        save_book(book)

        return {"message": "success"}, 200
    except Exception as e:
        return {"message": f"Fehler: {e}"}, 500


def create_book(data):
    try:
        book = Book.query.filter_by(isbn=data['isbn']).first()

        if not book:

            author = get_author_by_id(data['author_id'])
            if author is None:
                return {"message": "Den Author gibt es nicht"}, 409

            new_book = Book(
                isbn=data['isbn'],
                title=data['title'],
                description=data['description'],
                author_id=data['author_id'],
            )
            save_book(new_book)
            return {"message": "erstellt"}, 201
        else:
            return {"message": "Buch existiert bereits"}, 409
    except Exception as e:
        return {"message": f"Fehler: {e}"}, 500
