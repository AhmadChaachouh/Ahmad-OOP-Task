# src/robots/cleaning_robot.py

from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name: str, cleaning_tool: str):
        super().__init__(name)
        self._cleaning_tool = cleaning_tool

    @property
    def cleaning_tool(self) -> str:
        return self._cleaning_tool

    def work(self) -> None:
        if self._battery_level >= 20:
            self._battery_level -= 20
            self._status = "working"
            print(f"{self._name} is cleaning with {self._cleaning_tool}.")
        else:
            print(f"{self._name} does not have enough battery to clean.")
