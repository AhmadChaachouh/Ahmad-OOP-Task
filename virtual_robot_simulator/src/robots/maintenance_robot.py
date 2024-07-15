# src/robots/maintenance_robot.py

from .cleaning_robot import CleaningRobot
from .cooking_robot import CookingRobot

class MaintenanceRobot(CleaningRobot, CookingRobot):
    def __init__(self, name: str, cleaning_tool: str, cooking_skill: str):
        super().__init__(name, cleaning_tool, cooking_skill)

    def multi_task(self) -> None:
        # Perform cleaning task
        if self.battery_level >= 20:
            self.battery_level -= 20
            print(f"{self.name} is cleaning with {self.cleaning_tool}.")
        else:
            print(f"{self.name} does not have enough battery to clean.")
        
        # Perform cooking task
        if self.battery_level >= 30:
            self.battery_level -= 30
            print(f"{self.name} is cooking with {self.cooking_skill} skills.")
        else:
            print(f"{self.name} does not have enough battery to cook.")
