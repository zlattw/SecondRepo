

class NameSurname:
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname

class Student:
    student_amount = 0
    def HappyBirthday(self):
        self.age +=1
        print(f"Happy Birthday to {self.name}. Now you {self.age}!")

    def __init__ (self, name, surname,age, height, school = "itstep"):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.school = school
        Student.student_amount += 1


    def printStudent(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")

    def School(self):
        return bool(self.school)

    def grade_point_average(self, grade):
        if grade == 12:
            print("Відмінно")
        elif grade >= 10:
            print("Добре")
        elif grade >= 7:
            print("Задовільно")
        elif grade >= 4:
            print("Погано")
        elif grade >= 1:
            print("Дуже погано")



print(f"Before creating Student object - {Student.student_amount}")
Zlata = Student("Zlata", "Samuseva", 15, 175, )
print(f"Before creating Student object - {Student.student_amount}")
first_student = Student(input("Enter name - "), input("Enter surname - "), input("Enter age - "), input("Enter height - "))


print(Zlata.name, Zlata.surname, Zlata.age, Zlata.height)
print(first_student.name, first_student.surname, first_student.age, first_student.height)
Zlata.printStudent()
print(f"Student amount - {Student.student_amount}")
print(f"After creating Student object - {Student.student_amount}")

print(Zlata.School())
average_grade = int(input("Введіть середній бал студента - "))
print(Zlata.grade_point_average(average_grade))