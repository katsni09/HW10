class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} I'm {self.age} .")

class Teacher(Person):
    def __init__(self, name, age, subject_taught):
        super().__init__(name, age)
        self.subject_taught = subject_taught

    def teach(self):
        print(f"I teach {self.subject_taught}.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"My student ID nr is {self.student_id}.")

class Subject:
    def __init__(self, name):
        self.name = name

class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def list_teachers(self):
        print(f"Teachers {self.name}:")
        for teacher in self.teachers:
            print(teacher.name)

    def list_students(self):
        print(f"Students {self.name}:")
        for student in self.students:
            print(student.name)

    def list_subjects(self):
        print(f"Subjects {self.name}:")
        for subject in self.subjects:
            print(subject.name)

reading_teacher = Teacher("Emma", 39, "Reading")
math_teacher = Teacher("Olga", 70, "Math")
geo_teacher = Teacher("Jan", 35, "Geography")

alice = Student("Alice", 21, "12345")
alex = Student("Alex", 20, "56789")

read = Subject("Reading")
math = Subject("Math")
geo = Subject("Geography")

academy = Academy("Academy")

academy.add_teacher(reading_teacher)
academy.add_teacher(math_teacher)
academy.add_teacher(geo_teacher)

academy.add_student(alice)
academy.add_student(alex)

academy.add_subject(read)
academy.add_subject(math)
academy.add_subject(geo)

academy.list_teachers()
academy.list_students()
academy.list_subjects()


math_teacher.introduce()
math_teacher.teach()
alice.introduce()
alice.study()
