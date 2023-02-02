from oop.oop_exams.retake_exam_22_august_2022.project import Employee
from oop.oop_exams.retake_exam_22_august_2022.project import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
