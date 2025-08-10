from models import Student

def add_student(session):
    name = input("Enter name: ")
    email = input("Enter email: ")
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    print("Student added successfully!")

def view_students(session):
    students = session.query(Student).all()
    for student in students:
        print(f"{student.id}: {student.name} - {student.email}")
