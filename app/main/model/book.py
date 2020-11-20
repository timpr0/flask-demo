from .. import db


class Book(db.Model):

    __tablename__ = 'Books'

    isbn = db.Column('ISBN', db.Integer, unique=True, primary_key=True)
    title = db.Column('Title', db.Text, nullable=False)
    description = db.Column('Description', db.Text, nullable=False)
    author_id = db.Column('Author', db.Integer, db.ForeignKey('Authors.ID'), nullable=False)

    def __repr__(self) -> str:
        return f"<Book isbn='{self.isbn}' " \
               f"title='{self.title}' " \
               f"description='{self.description}' " \
               f"author_id='{self.author_id}'>"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Book):
            return NotImplemented

        return self.isbn == o.isbn \
            and self.title == o.title \
            and self.description == o.description \
            and self.author_id == o.author_id

    def __hash__(self) -> int:
        return hash((self.isbn, self.title, self.description, self.author_id))
