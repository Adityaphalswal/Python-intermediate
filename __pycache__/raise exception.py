class AdultException(Exception):
    pass

class Person:
    def __init__(self, name , age):
        self.name= name
        self.age=age

    def get_minor_age(self):
        if int(self.age)>=18:
            raise AdultException
        else:
            return self.age
    
    def display(self):
        try:
            print(f"age ->{self.get_minor_age()}")
        except AdultException:
            print("Person is an adult")
        finally:
            print(f"name ->{self.name}")

#Exception raised
Person("aditya", 20).display

#No Exception
Person("bhupesh", 17).display