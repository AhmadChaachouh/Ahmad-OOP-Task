# tests/test_base_robot.py

import unittest
from robots.base_robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(name="TestBot")

    def test_initial_status(self):
        self.assertEqual(self.robot.status, "idle")

    def test_charge(self):
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "charging")

if __name__ == '__main__':
    unittest.main()
