# src/robots/cleaning_robot.py

from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name: str, cleaning_tool: str, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self._cleaning_tool = cleaning_tool

    @property
    def cleaning_tool(self) -> str:
        return self._cleaning_tool

    def work(self) -> None:
        if self.battery_level >= 20:
            self.battery_level -= 20
            self._status = "working"
            print(f"{self.name} is cleaning with {self.cleaning_tool}.")
        else:
            print(f"{self.name} does not have enough battery to clean.")
