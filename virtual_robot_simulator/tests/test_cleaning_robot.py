# tests/test_cleaning_robot.py

import unittest
from robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):
    def setUp(self):
        self.cleaning_robot = CleaningRobot(name="CleanBot", cleaning_tool="vacuum")

    def test_initial_status(self):
        self.assertEqual(self.cleaning_robot.status, "idle")
        self.assertEqual(self.cleaning_robot.battery_level, 100)
        self.assertEqual(self.cleaning_robot.cleaning_tool, "vacuum")

    def test_work(self):
        self.cleaning_robot.work()
        self.assertEqual(self.cleaning_robot.battery_level, 80)
        self.assertEqual(self.cleaning_robot.status, "working")

    def test_charge(self):
        self.cleaning_robot.charge()
        self.assertEqual(self.cleaning_robot.battery_level, 100)
        self.assertEqual(self.cleaning_robot.status, "charging")

if __name__ == '__main__':
    unittest.main()
