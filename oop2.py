# creat a class called person with name, age, gender as
# the attributes, a constructor, a method, an object



class Person:

    def __init__(self, name1, age, gender):
        self.name1 = name1
        self.age = age
        self.gender = gender

    # method
    def display(self):
        print(f"I am {self.name1}, {self.age}, {self.gender}")

# instance(object)
myobj = Person("Harry",15,"Male")
myobj.display()
