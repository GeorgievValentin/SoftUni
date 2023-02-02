from oop.oop_exams.retake_exam_22_august_2022.project import FormulaTeam


class RedBullTeam(FormulaTeam):

    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def sponsors(self):
        return {
            "Oracle": {
                1: 1_500_000,
                2: 800_000
            },
            "Honda": {
                8: 20_000,
                10: 10_000
            }
        }

    @property
    def expenses_for_race(self):
        return 250_000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for sponsor in self.sponsors.values():
            for position in sponsor:
                if race_pos <= position:
                    revenue += sponsor[position]
                    break

        revenue -= self.expenses_for_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

