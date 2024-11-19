class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        print(f"Name: [{self.name}], Age: [{self.age}], Gender: [{self.gender}]")

class Student(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.student_id = ""
        self.course = ""
        self.grades = []
        self.avg


    def set_student_details(self,student_id, course): 
        self.student_id = student_id
        self.course = course

    def addgrade(self, grade):
        grades = []
        self.grades = grades.append(grade)

    def calculate_average_grade(self):
        if len(self.grades) >= 1:
         self.avg = sum(self.grades())/ len(self.grades)
         print(self.avg)
        else:
            print(0)
        
    def get_student_summary(self):
        print(f"Name:{self.name}, Age:{self.age}, Gender:{self.gender}, Student ID:{self.student_id}, Course:{self.course}, Average Grade:{self.avg}") 

class Professor(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.staff_id = ""
        self.department = ""
        self.salary = 0


    def set_professor_details(staff_id, department, salary): 


