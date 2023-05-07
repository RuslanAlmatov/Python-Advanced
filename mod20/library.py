import datetime

from flask import Flask, request
from sqlalchemy import create_engine, Column, Integer, Text, Date, Float, Boolean, DateTime
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///library.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

Base = declarative_base()


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.count}, {self.release_date}, {self.author_id}"


class Authors(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.surname}"


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.phone}, {self.email}, {self.average_score}, {self.scholarship}"

    @classmethod
    def get_scholarship_students(cls):
        return session.query(Students).filter(Students.scholarship == True).all()

    @classmethod
    def get_better_score(cls, score):
        return session.query(Students).filter(Students.average_score > score).all()


class Receiving_books(Base):
    __tablename__ = "receiving_books"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    def __repr__(self):
        return f"{self.book_id}, {self.student_id}, {self.date_of_issue}, {self.date_of_return}"

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return:
            return (self.date_of_return - self.date_of_issue).day
        else:
            return (datetime.datetime.now() - self.date_of_issue).days


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route("/get_all_books", methods=["GET"])
def get_all_books():
    books = session.query(Books).all()
    list_of_books = []
    for book in books:
        list_of_books.append(book)
    return list_of_books, 200


@app.route("/debtors", methods=["GET"])
def get_debtors():
    debtors = session.query(Receiving_books).filter(Receiving_books.date_of_return == None).all()
    debtors_list = []
    for debtor in debtors:
        if debtor.count_date_with_book > 14:
            debtors_list.append(debtor)
    return debtors_list, 200


@app.route("/lend_book", methods=["POST"])
def lend_book():
    book_id = request.form.get("book_id", type=int)
    student_id = request.form.get("student_id", type=int)
    new_lend_book = Receiving_books(book_id=book_id,
                                    student_id=student_id,
                                    date_of_issue=datetime.datetime.now())
    session.add(new_lend_book)
    session.commit()

    return "Книга выдана", 201


@app.route("/turn_book", methods=["POST"])
def turn_book():
    try:
        book_id = request.form.get("book_id", type=int)
        student_id = request.form.get("student_id", type=int)
        book = session.query(Receiving_books).filter(Receiving_books.book_id == book_id,
                                                     Receiving_books.student_id == student_id).one()
        book.date_of_return = datetime.datetime.now()
        session.commit()
        return f"Книга {book_id} сдана"
    except NoResultFound:
        return "Данная связка не найдена", 404
    except MultipleResultsFound:
        return "Ошибка уникальности связки"


if __name__ == "__main__":
    app.run()
