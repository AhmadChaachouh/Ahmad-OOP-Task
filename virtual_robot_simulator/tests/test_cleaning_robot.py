# tests/test_cleaning_robot.py

import unittest
from robots.cleaning_robot import CleaningRobot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CleaningRobot(name="TestBot")

    def test_initial_status(self):
        self.assertEqual(self.robot.status, "idle")

    def test_charge(self):
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "charging")

if __name__ == '__main__':
    unittest.main()
