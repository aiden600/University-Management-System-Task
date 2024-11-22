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
        self.avg = 0


    def set_student_details(self,student_id, course): 
        self.student_id = student_id
        self.course = course

    def addgrade(self, grade):
         self.grades.append(grade)
         print(self.grades)
         

    def calculate_average_grade(self):
        if len(self.grades) >= 1:
         self.avg = sum(self.grades)/ len(self.grades)
         print (self.avg)
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


    def set_professor_details(self,staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    
    def give_feedback(self,student, feedback):
        self.student = student
        self.feedback = feedback
        print(f"Given feedback for {student.name}: {self.feedback}")

    def increase_salary(self,percentage):
        percentage = percentage/100
        percentage += 1
        self.salary = self.salary * percentage

    def get_professor_summary(self):
        print(f"Name:{self.name}, Age:{self.age}, Gender:{self.gender}, Staff ID:{self.staff_id}, Department:{self.department}, Salary:{self.salary}") 


class Administrator(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.admin_id = ""
        self.office = ""
        self.years_of_service = 0

    def set_admin_details(self,admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def increment_service_years(self):
        self.years_of_service += 1
    
    def get_admin_summary(self):
        print(f"Name:{self.name}, Age:{self.age}, Gender:{self.gender}, Admin ID:{self.admin_id}, Office:{self.office}, Years of Service:{self.years_of_service}") 


professor1 = Professor("Mehran",20,"Male")
professor1.set_professor_details("P1234","Maths",100000)

student1 = Student("Alice Johnson", 20, "Female")
student1.set_student_details("S5678", "Physics")

professor2 = Professor("A",90,"Male")
professor2.set_professor_details("A8376","Computer Science",190000)

student2 = Student("Tonye",43,"Male")
student2.set_student_details("T7635","Finance")

admin1 = Administrator("John",70,"Male")
admin1.set_admin_details("R4253","L20",19)

student1.addgrade(9)
student1.addgrade(7)
student1.calculate_average_grade()


