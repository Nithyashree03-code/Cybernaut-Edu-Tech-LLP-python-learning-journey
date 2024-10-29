class Dog:
    def sound(self):
        return "Woof!"
class Cat:
    def sound(self):
        return "Meow!"
class Cow:
    def sound(self):
        return "Moo!"
def animal_sound(animal):
    print(animal.sound())
dog = Dog()
cat = Cat()
cow = Cow()
animal_sound(dog)  
animal_sound(cat)  
animal_sound(cow)  
