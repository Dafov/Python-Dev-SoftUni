class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + birth_year


student_name = input()
student_last_name = input()
student_b_year = input()

new_student = Student(student_name, student_last_name, student_b_year)

print(new_student.id)