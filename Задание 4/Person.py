from abc import ABC, abstractmethod
from datetime import datetime, date


class Person(ABC):

    TOTAL_PERSONS = 0
    PERSONS = []

    def __init__(self, name, date_of_birth, faculty):
        self._name = name
        self._date_of_birth = date_of_birth
        self._faculty = faculty
        Person.TOTAL_PERSONS += 1
        Person.PERSONS += [self]

    def calculate_age(self):
        born = datetime.strptime(self._date_of_birth, "%d %m %Y")
        today = date.today()
        extra_year = 1 if ((today.month, today.day) < (born.month, born.day)) else 0
        age = today.year - born.year - extra_year
        return age

    def get_age(self):
        return f'{self._name}: {self.calculate_age()} years'

    @classmethod
    def found_persons(cls, a, b):
        info = []
        for p in cls.PERSONS:
            if a <= p.calculate_age() <= b:
                info += [p]
        return info

    @abstractmethod
    def info(self):
        return f'Name: {self._name}, Date of birth: {self._date_of_birth}, Faculty: {self._faculty}'


class Applicant(Person):

    APPLICANTS = []

    def __init__(self, name, date_of_birth, faculty):
        Person.__init__(self, name, date_of_birth, faculty)
        Applicant.APPLICANTS += [self]

    def info(self):
        return Person.info(self) + f', Age: {Applicant.calculate_age(self)}'


class Student(Person):

    STUDENTS = []

    def __init__(self, name, date_of_birth, faculty, course):
        Person.__init__(self, name, date_of_birth, faculty)
        self._course = course
        Student.STUDENTS += [self]

    def info(self):
        return Person.info(self) + f', Course: {self._course}, Age: {Student.calculate_age(self)}'


class Teacher(Person):

    TEACHERS = []

    def __init__(self, name, date_of_birth, faculty, position, experience):
        Person.__init__(self, name, date_of_birth, faculty)
        self._position = position
        self._experience = experience
        Teacher.TEACHERS +=[self]

    def info(self):
        return Person.info(self) + f', Position: {self._position}, Experience: {self._experience}, Age: {Teacher.calculate_age(self)}'


teacher1 = Teacher('teacher1', '12 01 1965', 'Informatics', 'Dean', '35')
teacher2 = Teacher('teacher2', '22 05 1970', 'Maths', 'Dean', '25')
teacher3 = Teacher('teacher3', '01 11 1985', 'Maths', 'Teacher', '15')
teacher4 = Teacher('teacher4', '20 10 1980', 'Physics', 'Teacher', '12')

applicant1 = Applicant('applicant1', '05 04 2003', 'Physics')
applicant2 = Applicant('applicant2', '05 04 2002', 'Maths')
applicant3 = Applicant('applicant3', '05 04 2004', 'Informatics')

student1 = Student('student1', '05 04 1999', 'Physics', '2')
student2 = Student('student2', '05 04 2000', 'Informatics', '1')
student3 = Student('student3', '05 04 1996', 'Maths', '5')

for i in Person.PERSONS:
    print(i.info())

print(Person.TOTAL_PERSONS)

for i in Person.found_persons(20, 50):
    print(i.info())


print(teacher1.get_age())