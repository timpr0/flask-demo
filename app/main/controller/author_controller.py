from flask import request
from flask_restplus import Resource

from ..utils.dto import AuthorDao
from ..service.author_service import get_all_authors, create_author, get_author_by_id, update_author

api = AuthorDao.api
_author = AuthorDao.author


@api.route('/')
class AuthorList(Resource):
    @api.doc('list_of_authors')
    @api.marshal_list_with(_author, envelope='authors')
    def get(self):
        return get_all_authors()

    @api.response(201, 'Author erstellt')
    @api.doc('Einen neuen Author erstellen')
    @api.expect(_author, validate=True)
    def post(self):
        data = request.json
        return create_author(data=data)


@api.route('/<author_id>')
@api.param('author_id', 'ID des Authors')
@api.response(404, 'Der Author wurde nicht gefunden.')
class Author(Resource):
    @api.doc('get a user')
    @api.marshal_with(_author)
    def get(self, author_id):
        author = get_author_by_id(author_id)
        if not author:
            return {"message": "Author nicht gefunden"}, 404
        else:
            return author

    @api.doc("update author")
    def put(self, author_id):
        data = request.json
        if data is None:
            return {"message": "Ungueltiges Format"}, 400

        return update_author(author_id, data)



