from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_student(name, age):
    student = Student(name=name, age=age)
    session.add(student)
    session.commit()

def show_students():
    for student in session.query(Student).all():
        print(student.id, student.name, student.age)

def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()

# Example usage:
if __name__ == '__main__':
    add_student("Alice", 20)
    add_student("Bob", 22)
    print("All students:")
    show_students()
    print("Deleting student with ID 1")
    delete_student(1)
    print("All students after deletion:")
    show_students()