import json
from flask import Flask, render_template, request
from peewee import *
from models import BaseModel,Books,Students,BooksToStudents
from flask_peewee.rest import RestAPI


app = Flask(__name__)
app.config.from_object(__name__)


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


@app.route('/library/books/<book_id>/', methods=['DELETE'])
def del_book(book_id):
    query = Books.delete().where(Books.id==book_id)
    query.execute()
    return json.dumps({'message': 'Successfully deleted book with ID {}'.format(book_id)})

@app.route('/library/students/<student_id>/', methods=['GET'])
@app.route('/library/students/', methods=['GET'], defaults={'student_id': None})
def get_students(student_id):
    students = []
    if not student_id:
        students_select_obj = Students.select()
    else:
        students_select_obj = Students.select().where(Students.id==student_id)
    for each_student in students_select_obj:
        students.append({x: each_student.__getattribute__(x) for x in [
                    'id',
                    'name',
                    'course']})
    return json.dumps(students)


@app.route('/library/students', methods=['PUT'])
def insert_students():
    data = request.json
    data = json.load(request.data) 
    Students.insert(data).execute()
    return json.dumps({'message': 'Successfully inserted student with ID {}'.format(student_id)})


@app.route('/library/students/<student_id>/',methods=['DELETE'])
def del_students():
    query = Students.delete().where(Students.id==student_id)
    query.execute()
    return json.dumps({'message': 'Successfully deleted student with ID {}'.format(student_id)})


@app.route('/library/bookstostudents/<book_id>/', methods=['GET'])
@app.route('/library/bookstostudents/', methods=['GET'], defaults={'book_id': None})
def get_books_to_students(book_id):
    books_to_students = []
    if not book_id:
        books_select_obj = BooksToStudents.select()
    else:
        books_select_obj = BooksToStudents.select().where(BooksToStudents.id==book_id)
    for each_book in books_select_obj:
        books_to_students.append({x: each_book.__getattribute__(x) for x in [
                                 'actual_return_date',
                                 'received_date',
                                 'return_date']})
    return json.dumps(books)


@app.route('/library/bookstostudents',methods=['PUT'])
def insert_books_to_students():
    data = request.json
    data = json.loads(request.data)
    BooksToStudents.insert(data).execute()
    # TODO: Change to get the id and return as JSON 
    return json.dumps({'message': 'Successfully inserted information with ID {}'.format(book_id)})

@app.route('/library/bookstostudents/<book_id>/',methods=['DELETE'])
def del_books_to_students():
    query = BooksToStudents.delete().where(BooksToStudents.id==book_id)
    query.execute()
    return json.dumps({'message': 'Successfully deleted information with ID {}'.format(book_id)})


if __name__ == '__main__':
    app.run()
