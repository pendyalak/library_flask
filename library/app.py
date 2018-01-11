import json
from flask import Flask, render_template, request
from peewee import *
from models import BaseModel,Books,Students,BooksToStudents
from flask_peewee.rest import RestAPI


app = Flask(__name__)
app.config.from_object(__name__)

# TODO: same get for students and books_to_students
# TODO: delete for books, students and books_to_students
@app.route('/library/books/<book_id>/', methods=['GET'])
@app.route('/library/books/', methods=['GET'], defaults={'book_id': None})
def get_books(book_id):
    books = []
    if not book_id:
        books_select_obj = Books.select()
    else:
        books_select_obj = Books.select().where(Books.id==book_id)
    for each_book in books_select_obj:
        books.append({x: each_book.__getattribute__(x) for x in [
            'id',
            'name',
            'isbn',
            'author',
            'course']})
    return json.dumps(books)


@app.route('/library/books', methods=['PUT'])
def insert_books():
    data = request.json
    data = json.loads(request.data)
    book_id = Books.insert(data).execute()
    return json.dumps({'message': 'Successfully inserted book with ID {}'.format(book_id)})


@app.route('/library/students', methods=['PUT'])
def insert_students():
    data = request.json
    data = json.load(request.data)
    # TODO: Change to get the id and return as JSON 
    Students.insert(data).execute()
    return 'Success'


@app.route('/library/bookstostudents',methods=['PUT'])
def insert_books_to_students():
    data = request.json
    data = json.loads(request.data)
    BooksToStudents.insert(data).execute()
    # TODO: Change to get the id and return as JSON 
    return 'Success'


if __name__ == '__main__':
    app.run()
