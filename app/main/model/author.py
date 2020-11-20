from .. import db


class Author(db.Model):

    __tablename__ = 'Authors'

    id = db.Column('ID', db.Integer, unique=True, primary_key=True)
    name = db.Column('Name', db.Text, nullable=False)
    last_name = db.Column('Lastname', db.Text,  nullable=False)

    def __repr__(self):
        return f"<Author id='{self.id}' name='{self.name}' last_name='{self.last_name}'"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Author):
            return NotImplemented

        return self.id == o.id and self.name == o.name and self.last_name == o.last_name

    def __hash__(self) -> int:
        return hash((self.id, self.name, self.last_name))
