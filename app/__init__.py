from flask_restplus import Api
from flask import Blueprint

from .main.controller.author_controller import api as authors_ns
from .main.controller.book_controller import api as books_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(authors_ns, path='/authors')
api.add_namespace(books_ns, path='/books')
