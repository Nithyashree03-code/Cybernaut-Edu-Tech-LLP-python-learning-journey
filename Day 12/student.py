class Student:
    count = 0  
    def __init__(self, name):
        self.name = name
        Student.count += 1 
        self.display_name()
    def display_name(self):
        print(f"Student's Name: {self.name}")
    @classmethod
    def number_of_students(cls):
        return cls.count
student1 = Student("Nithya")
student2 = Student("Aarifa")
student3 = Student("Mekala")
print(f"Total number of students: {Student.number_of_students()}")
