from unittest import TestCase, main

# from oop.lab_ex_10_testing.hero.project.hero import Hero
from project.hero import Hero

class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero("hero", 1, 50, 10)
        self.enemy = Hero("enemy", 1, 60, 10)

    def test_correct_initialization(self):
        self.assertEqual("hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(50, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_fight_yourself_raises(self):
        self.enemy.username = "hero"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_fight_with_zero_hero_health_raise(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_fight_with_negative_hero_health_raise(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_fight_with_zero_enemy_health_raise(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight enemy. He needs to rest", str(ex.exception))

    def test_fight_with_negative_enemy_health_raise(self):
        self.enemy.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight enemy. He needs to rest", str(ex.exception))

    def test_correct_hero_player_health_after_fight(self):
        self.hero.battle(self.enemy)
        self.assertEqual(40, self.hero.health)

    def test_correct_players_health_decrease_and_return_after_fight(self):
        self.hero.health = 1
        self.enemy.health = 1

        result = self.hero.battle(self.enemy)
        self.assertEqual(-9, self.enemy.health)
        self.assertEqual(-9, self.hero.health)
        self.assertEqual("Draw", result)

    def test_correct_hero_win_battle(self):
        self.enemy.health = 10
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(45, self.hero.health)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual("You win", result)

    def test_correct_enemy_win_battle(self):
        self.hero.health = 10
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_correct_return__str__(self):
        result = str(self.hero)
        excepted = "Hero hero: 1 lvl\n" \
                   "Health: 50\n" \
                   "Damage: 10\n"

        self.assertEqual(excepted, result)


if __name__ == "__main__":
    main()
