# src/robots/cooking_robot.py

from .base_robot import Robot

class CookingRobot(Robot):
    def __init__(self, name: str, cooking_skill: str, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self._cooking_skill = cooking_skill

    @property
    def cooking_skill(self) -> str:
        return self._cooking_skill

    def work(self) -> None:
        if self.battery_level >= 30:
            self.battery_level -= 30
            self._status = "working"
            print(f"{self.name} is cooking with {self.cooking_skill} skills.")
        else:
            print(f"{self.name} does not have enough battery to cook.")
