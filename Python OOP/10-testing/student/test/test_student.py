from unittest import TestCase, main

# from oop.lab_ex_10_testing.student.project.student import Student
from project.student import Student

class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("Pencho")
        self.student_with_course = Student("Gencho", {"oop": ["note"]})

    def test_correct_initialization(self):
        self.assertEqual("Pencho", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"oop": ["note"]}, self.student_with_course.courses)

    def test_enroll_correct_notes_to_existing_course(self):
        result = self.student_with_course.enroll("oop", ["note 1", "note 2"])
        self.assertEqual(["note", "note 1", "note 2"], self.student_with_course.courses["oop"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_new_course_and_notes_without_third_param(self):
        result = self.student.enroll("oop", ["note 1", "note 2"])
        self.assertEqual(["note 1", "note 2"], self.student.courses["oop"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_new_course_and_notes_with_third_param_Y(self):
        result = self.student.enroll("oop", ["note 1", "note 2"], "Y")
        self.assertEqual(["note 1", "note 2"], self.student.courses["oop"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_new_course_without_notes(self):
        result = self.student.enroll("oop", ["note"], "N")
        self.assertEqual([], self.student.courses["oop"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_to_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("oop", ["note", "note 1"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.add_notes("oop", "note 1")
        self.assertEqual(["note", "note 1"], self.student_with_course.courses["oop"])
        self.assertEqual("Notes have been updated", result)

    def test_leave_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("oop")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_existing_course_correctly(self):
        result = self.student_with_course.leave_course("oop")
        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual("Course has been removed", result)


if __name__ == "__main__":
    main()
