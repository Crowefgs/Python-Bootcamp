class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Öğrenci No: {self.student_id}, İsim: {self.name}, Yaş: {self.age}")

student1 = Student(1, "Ahmet", 21)
student1.print_info()