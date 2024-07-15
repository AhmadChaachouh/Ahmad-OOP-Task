# src/robots/cooking_robot.py

from .base_robot import Robot

class CookingRobot(Robot):
    def __init__(self, name: str, cooking_skill: str):
        super().__init__(name)
        self._cooking_skill = cooking_skill

    @property
    def cooking_skill(self) -> str:
        return self._cooking_skill

    def work(self) -> None:
        if self._battery_level >= 30:
            self._battery_level -= 30
            self._status = "working"
            print(f"{self._name} is cooking with {self._cooking_skill} skills.")
        else:
            print(f"{self._name} does not have enough battery to cook.")
