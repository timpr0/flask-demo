from flask_restplus import Namespace, fields


class AuthorDao:
    api = Namespace('author', description='author operations')
    author = api.model('author', {
        'author_id': fields.Integer(attribute="id", description='author db id'),
        'name': fields.String(required=True),
        'last_name': fields.String(required=True)
    })


class BookDao:
    api = Namespace('book', description='book operations')
    book = api.model('book', {
        'isbn': fields.Integer(attribute='isbn', required=True),
        'title': fields.String(required=True),
        'description': fields.String(required=True),
        'author_id': fields.Integer(required=True),
    })
