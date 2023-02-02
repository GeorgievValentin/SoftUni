from unittest import TestCase, main

# from oop.oop_exams.exam_11_december_2021.tests.project.team import Team
from project.team import Team


class TeamTest(TestCase):
    def setUp(self):
        self.team = Team("team")
        self.team_ = Team("levski")

    def test_correct_initialization(self):
        self.assertEqual("team", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = "team 1"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_existing_members(self):
        self.team.members = {
            "Member_1": 21,
            "Member_2": 22,
            "Member_3": 23
        }
        self.team.add_member(Member_2=22, Member_3=23)
        expected = {
            "Member_1": 21,
            "Member_2": 22,
            "Member_3": 23
        }
        result = self.team.members
        self.assertEqual(expected, result)

    def test_add_non_existing_members(self):
        self.team.members = {
            "Member_1": 21,
            "Member_2": 22,
            "Member_3": 23
        }
        self.team.add_member(Member_4=22, Member_5=23)

        expected = {
            "Member_1": 21,
            "Member_2": 22,
            "Member_3": 23,
            "Member_4": 22,
            "Member_5": 23
        }
        result = self.team.members
        self.assertEqual(expected, result)

    def test_remove_non_existing_member(self):
        self.team.add_member(Member_4=22, Member_5=23)
        result = self.team.remove_member("Member_1")
        self.assertEqual({"Member_4": 22, "Member_5": 23}, self.team.members)
        self.assertEqual("Member with name Member_1 does not exist", result)

    def test_remove_existing_member(self):
        self.team.add_member(Member_4=22, Member_5=23)
        result = self.team.remove_member("Member_4")
        self.assertEqual({"Member_5": 23}, self.team.members)
        self.assertEqual("Member Member_4 removed", result)

    def test__gt__method_False(self):
        self.team.add_member(Member_4=22, Member_5=23)
        self.team_.add_member(Member_1=22, Member_2=23, Member_3=20)
        result = self.team > self.team_
        self.assertEqual(False, result)

    def test__gt__method_False_equal(self):
        self.team.add_member(Member_4=22, Member_5=23)
        self.team_.add_member(Member_1=22, Member_2=23)
        result = self.team > self.team_
        self.assertEqual(False, result)

    def test___gt__method_True(self):
        self.team.add_member(Member_4=22, Member_5=23, Member_3=20)
        self.team_.add_member(Member_1=22, Member_2=23)
        result = self.team > self.team_
        self.assertEqual(True, result)

    def test__len__method(self):
        self.team.add_member(Member_4=22, Member_5=23, Member_3=20)
        self.assertEqual(3, len(self.team))

    def test__add__method(self):
        self.team.add_member(Member_4=22)
        self.team_.add_member(Member_1=22, Member_2=23)
        new_team = self.team + self.team_

        expected = {
            "Member_4": 22,
            "Member_1": 22,
            "Member_2": 23,
        }
        self.assertEqual("teamlevski", new_team.name)
        self.assertEqual(expected, new_team.members)
        self.assertEqual(3, len(new_team))

    def test__str__method(self):
        self.team.add_member(Member_1=22, Member_2=23, Pencho=23)
        expected = "Team name: team\n" \
                   "Member: Member_2 - 23-years old\n" \
                   "Member: Pencho - 23-years old\n" \
                   "Member: Member_1 - 22-years old"
        self.assertEqual(expected, str(self.team))


if __name__ == "__main__":
    main()
