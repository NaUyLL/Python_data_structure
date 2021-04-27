import datetime

class Person:
    _num = 0

    def __init__(self):
        Person._num += 1

    @classmethod
    def count_person(cls):
        return Person._num

class Student(Person):
    pass

class Staff(Person):
    pass



if __name__ == "__main__":
    a = Staff()
    b = Student()
    print(Person.count_person())