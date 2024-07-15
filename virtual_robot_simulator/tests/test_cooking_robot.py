# tests/test_cooking_robot.py

import unittest
from robots.cooking_robot import CookingRobot

class TestCookingRobot(unittest.TestCase):
    def setUp(self):
        self.cooking_robot = CookingRobot(name="CookBot", cooking_skill="expert")

    def test_initial_status(self):
        self.assertEqual(self.cooking_robot.status, "idle")
        self.assertEqual(self.cooking_robot.battery_level, 100)
        self.assertEqual(self.cooking_robot.cooking_skill, "expert")

    def test_work(self):
        self.cooking_robot.work()
        self.assertEqual(self.cooking_robot.battery_level, 70)
        self.assertEqual(self.cooking_robot.status, "working")

    def test_charge(self):
        self.cooking_robot.charge()
        self.assertEqual(self.cooking_robot.battery_level, 100)
        self.assertEqual(self.cooking_robot.status, "charging")

if __name__ == '__main__':
    unittest.main()
