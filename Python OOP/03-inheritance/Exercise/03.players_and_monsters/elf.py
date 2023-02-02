from oop.oop_exams.retake_exam_22_august_2022.project import Hero


class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

