

class NameSurname:
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname

class Student:
    student_amount = 0
    birthday = 0
    def HappyBirthday(self):
        self.age +=1
        print(f"Happy Birthday to {self.ns.name}. Now you {self.age}!")

    def __init__ (self,name, surname,age, height):
        self.ns = NameSurname(name, surname)
        self.age = age
        self.height = height
        Student.student_amount += 1


    def printStudent(self):
        print(f"Name: {self.ns.name}")
        print(f"Surname: {self.ns.surname}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")

print(f"Before creating Student object - {Student.student_amount}")
Zlata = Student("Zlata", "Samuseva", 12, 175)
print(f"Before creating Student object - {Student.student_amount}")
first_student = Student(input("Enter name - "), input("Enter surname - "), input("Enter age - "), input("Enter height - "))


print(Zlata.name, Zlata.surname, Zlata.age, Zlata.height)
print(first_student.name, first_student.surname, first_student.age, first_student.height)
Zlata.printStudent()
print(f"Student amount - {Student.student_amount}")
print(f"After creating Student object - {Student.student_amount}")

