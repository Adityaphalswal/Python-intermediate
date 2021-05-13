class Teacher:
    def teachers_action(self):
        print("i can teach")

class Engineer:
    def Engineers_action(self):
        print("i can code")

class Youtuber:
    def tuber_action(self):
        print("I an code and teach")

class Person(Teacher, Engineer, Youtuber):
    pass

coder = Person()
coder.teachers_action
coder.Engineers_action
coder.tuber_action
