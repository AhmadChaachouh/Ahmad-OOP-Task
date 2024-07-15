# src/main.py

from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot

def main():
    cleaner = CleaningRobot(name="CleanBot", cleaning_tool="vacuum")
    chef = CookingRobot(name="CookBot", cooking_skill="expert")

    cleaner.report_status()
    cleaner.work()
    cleaner.report_status()
    cleaner.charge()
    cleaner.report_status()

    chef.report_status()
    chef.work()
    chef.report_status()
    chef.charge()
    chef.report_status()

if __name__ == "__main__":
    main()
