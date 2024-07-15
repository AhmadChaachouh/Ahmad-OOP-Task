# tests/test_maintenance_robot.py

import unittest
from robots.maintenance_robot import MaintenanceRobot

class TestMaintenanceRobot(unittest.TestCase):
    def setUp(self):
        self.maintenance_robot = MaintenanceRobot(name="MaintBot", cleaning_tool="mop", cooking_skill="intermediate")

    def test_initial_status(self):
        self.assertEqual(self.maintenance_robot.status, "idle")
        self.assertEqual(self.maintenance_robot.battery_level, 100)
        self.assertEqual(self.maintenance_robot.cleaning_tool, "mop")
        self.assertEqual(self.maintenance_robot.cooking_skill, "intermediate")

    def test_multi_task(self):
        self.maintenance_robot.multi_task()
        self.assertEqual(self.maintenance_robot.battery_level, 50)
        self.assertEqual(self.maintenance_robot.status, "working")

    def test_charge(self):
        self.maintenance_robot.charge()
        self.assertEqual(self.maintenance_robot.battery_level, 100)
        self.assertEqual(self.maintenance_robot.status, "charging")

    def test_self_diagnose(self):
        self.maintenance_robot.battery_level = 10
        self.maintenance_robot.self_diagnose()

if __name__ == '__main__':
    unittest.main()
