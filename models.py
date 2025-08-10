from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    courses = relationship("Course", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("Student", back_populates="courses")