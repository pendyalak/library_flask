from peewee import *
import datetime
from settings import *

# TODO: find what *args and **kwargs?
database = MySQLDatabase(**LIBRARY_DATABASE)

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Books(BaseModel):
    author = CharField(null=True)
    course = CharField(null=True)
    isbn = CharField(null=True)
    name = CharField(null=True)

    class Meta:
        db_table = 'books'

class Students(BaseModel):
    course = CharField(null=True)
    name = CharField(null=True)

    class Meta:
        db_table = 'students'

class BooksToStudents(BaseModel):
    actual_return_date = DateTimeField(null=True)
    book = ForeignKeyField(db_column='book_id', null=True, rel_model=Books, to_field='id')
    received_date = DateTimeField(default=datetime.datetime.now)
    return_date = DateTimeField(default=datetime.datetime.now)
    student = ForeignKeyField(db_column='student_id', null=True, rel_model=Students, to_field='id')

    class Meta:
        db_table = 'books_to_students'

