# src/main.py

from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot
from robots.maintenance_robot import MaintenanceRobot

def main():
    cleaner = CleaningRobot(name="CleanBot", cleaning_tool="vacuum")
    chef = CookingRobot(name="CookBot", cooking_skill="expert")
    maintenance = MaintenanceRobot(name="MaintBot", cleaning_tool="mop", cooking_skill="intermediate")

    print("\n--- CleanBot Status ---")
    cleaner.report_status()
    cleaner.work()
    cleaner.report_status()
    cleaner.charge()
    cleaner.report_status()

    print("\n--- CookBot Status ---")
    chef.report_status()
    chef.work()
    chef.report_status()
    chef.charge()
    chef.report_status()

    print("\n--- MaintBot Status ---")
    maintenance.report_status()
    maintenance.multi_task()
    maintenance.report_status()
    maintenance.charge()
    maintenance.report_status()
    maintenance.self_diagnose()

if __name__ == "__main__":
    main()
