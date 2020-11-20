from app.main import db
from app.main.model.author import Author
from ..utils.dto import AuthorDao
from sqlalchemy import and_
from ..utils.exceptions import DatabaseException


def get_all_authors() -> [Author] or None:
    try:
        return Author.query.all()
    except Exception as e:
        raise DatabaseException(e)


def get_author_by_id(author_id: int) -> Author:
    try:
        return Author.query.filter_by(id=author_id).first()
    except Exception as e:
        raise DatabaseException(e)


def save_author(author: AuthorDao) -> None:
    db.session.add(author)
    db.session.commit()


def update_author(author_id, data):
    try:
        author = get_author_by_id(author_id)
        if not author:
            return {"message": "Author nicht gefunden"}, 404

        author.last_name = data['last_name']
        author.name = data['name']
        save_author(author)

        return {"message": "success"}, 200
    except Exception as e:
        return {"message": f"Fehler: {e}"}, 500


def create_author(data):
    try:
        author = Author.query.filter(
            and_(
                Author.name.ilike(data['name']),
                Author.last_name.ilike(data['last_name'])
            )).first()

        if not author:
            new_author = Author(
                name=data['name'],
                last_name=data['last_name'],
            )
            save_author(new_author)
            return {"message": "success"}, 201
        else:
            return {'message': 'Der Author existiert bereits'}, 409
    except Exception as e:
        return {"message": f"Fehler: {e}"}, 500
