class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id
    def introduce(self):
        parent_intro = super().introduce()  
        return f"{parent_intro} My student ID is {self.student_id}."
student = Student("Nithya", 20, "S12345")
print(student.introduce())
