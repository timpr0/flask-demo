from flask import request
from flask_restplus import Resource

from ..utils.dto import BookDao
from ..service.book_service import get_all_books, create_book, get_book_by_isbn, update_book

api = BookDao.api
_book = BookDao.book


@api.route('/')
class BookList(Resource):
    @api.doc('list_of_books')
    @api.marshal_list_with(_book, envelope='books')
    def get(self):
        return get_all_books()

    @api.response(201, 'Buch erstellt')
    @api.doc('Neues Buch erstellen')
    @api.expect(_book, validate=True)
    def post(self):
        data = request.json
        return create_book(data=data)


@api.route('/<book_isbn>')
@api.param('book_isbn', 'Die ISBN des Buchs')
@api.response(404, 'Buch nicht gefunden')
class Book(Resource):
    @api.doc('get buch')
    @api.marshal_with(_book)
    def get(self, book_isbn):
        book = get_book_by_isbn(book_isbn)
        if not book:
            return {"message": "Nicht gefunden"}, 404
        else:
            return book

    @api.doc("update book")
    def put(self, book_isbn):
        data = request.json
        if data is None:
            return {"message": "Ungueltiges Format"}, 400

        return update_book(book_isbn, data)
