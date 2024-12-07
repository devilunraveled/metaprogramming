
from classDecorators import classDecorator
from decorator import getNameDecorator

@classDecorator
class Student :
    count = 0
    print(f"Student Count = {count}")

    def __init__(self, name, age) :
        self.name = name
        self.age = age
        Student.count += 1
    
    @getNameDecorator
    def getName(self) :
        return self.name

    @staticmethod
    def findGPAFromGrade( grade : str ) :
        if grade == "A" :
            return 4.0
        elif grade == "B" :
            return 3.0
        else :
            return 1.0
        
    @classmethod
    def getStudentCount(cls) :
        return cls.count

if __name__ == "__main__" :
    print("Creating Student Object")
    student = Student("Devil Unraveled", 20)
    print("Accessing student's name")
    print(student.getName())
    print("Accessing student count")
    print(Student.getStudentCount())
    print("Accessing student's gpa")
    print(Student.findGPAFromGrade("A"))
