from robots.base_robot import BaseRobot

class CookingRobot(BaseRobot):
    def __init__(self, name: str, battery_level: int, status: str, cooking_skill:str) -> None:
        super().__init__(name, battery_level, status)
        self.cooking_skill = cooking_skill

    def work(self):
        if self.battery_level > 30:
            print("Let me cook...")
            self.battery_level -= 30
        else:
            print("Can't cook, battery too low!")
    
    


