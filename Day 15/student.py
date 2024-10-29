class Student:
    def __init__(self, name, age):
        self._name = name 
        self._age = age 
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_age(self):
        return self._age
    def set_age(self, age):
        if age >= 0: 
            self._age = age
        else:
            print("Age cannot be negative.")
student1 = Student("nithya", 20)
print("Name:", student1.get_name()) 
print("Age:", student1.get_age())   
student1.set_name("shree")
student1.set_age(22)
print("Updated Name:", student1.get_name())  
print("Updated Age:", student1.get_age())    
student1.set_age(-5)  
