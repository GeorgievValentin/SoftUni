from oop.oop_exams.retake_exam_22_august_2022.project import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


# person = Person("Peter", 25)
# child = Child("Peter Junior", 5)
# print(person.name)
# print(person.age)
# print(child.__class__.__bases__[0].__name__)
