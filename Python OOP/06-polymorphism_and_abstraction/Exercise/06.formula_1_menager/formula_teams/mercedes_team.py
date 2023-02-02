from oop.oop_exams.retake_exam_22_august_2022.project import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def sponsors(self):
        return {
            "Petronas": {
                1: 1_000_000,
                3: 500_000
            },
            "TeamViewer": {
                5: 100_000,
                7: 50_000
            }
        }

    @property
    def expenses_for_race(self):
        return 200_000

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
