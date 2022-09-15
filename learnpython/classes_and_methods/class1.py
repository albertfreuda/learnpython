class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is {} and I'm {} years old.".format(self.name,self.age))

p1 = Person("John",36)
p1.myfunc()

p1.age = 40
p1.myfunc()


