import logging
logging.basicConfig(level = logging.DEBUG,
                    filename = "logs.log",
                    filemode = "w",
                    format = "%(levelname)s:%(asctime)s - %(message)s")

class NameSurname:
    def __init__ (self, name, surname):
        if(type(name) != str):
            raise TypeError("Name is not a string")
        if (type(surname) != str):
            raise TypeError("Surname is not a string")
        self.name = name
        self.surname = surname

class Student:
    student_amount = 0
    birthday = 0
    def HappyBirthday(self):
        self.age += 1
        print(f"Happy Birthday to {self.ns.name}. Now you {self.age}!")

    def __init__ (self,name, surname,age, height):
        if (type(age) != int):
            raise TypeError("Incorrect age")
        if age <= 0:
            raise TypeError("Incorrect value")
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        Student.student_amount += 1
        logging.info(f"Create new student {Zlata.name} {Zlata.surname}")


    def printStudent(self):
        print(f"Name: {self.ns.name}")
        print(f"Surname: {self.ns.surname}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")

print(f"Before creating Student object - {Student.student_amount}")

logging.info("Program is started")
try:
    logging.debug("In progress..")
    Zlata = Student("Zlata", True, 0, 175)
    logging.info(f"Create new student {Zlata.name} {Zlata.surname}")

    print(f"Before creating Student object - {Student.student_amount}")

    first_student = Student(input("Enter name - "), input("Enter surname - "), int(input("Enter age - ")), int(input("Enter height - ")))
    print(Zlata.name, Zlata.surname, Zlata.age, Zlata.height)
    print(first_student.name, first_student.surname, first_student.age, first_student.height)
    Zlata.printStudent()

    print(f"Student amount - {Student.student_amount}")
    print(f"After creating Student object - {Student.student_amount}")
except Exception as error:
    print(error)
    logging.error(error)
logging.info("Program ended")
