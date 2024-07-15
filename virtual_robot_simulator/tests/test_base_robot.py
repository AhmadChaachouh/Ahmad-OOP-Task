# tests/test_base_robot.py

import unittest
from robots.base_robot import Robot
from robots.cleaning_robot import CleaningRobot  # Import a concrete class for testing

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CleaningRobot(name="TestBot", cleaning_tool="vacuum")  # Using CleaningRobot for instantiation

    def test_initial_status(self):
        self.assertEqual(self.robot.status, "idle")
        self.assertEqual(self.robot.battery_level, 100)

    def test_charge(self):
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "charging")

    def test_report_status(self):
        self.robot.report_status()

if __name__ == '__main__':
    unittest.main()
