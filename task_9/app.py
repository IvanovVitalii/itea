from mongoengine import *

connect('students_db')


class Student(Document):
    full_name = StringField(max_length=128)
    group = StringField(max_length=128)
    assessments = ListField()
    curator = StringField(max_length=128)
    faculty = StringField(max_length=128)


dict_student = {
    'full_name': 'Alex',
    'group': '945',
    'assessments': 5,
    'curator': 'Ivanov',
    'faculty': 'math',
}

student = Student(**dict_student).save()
