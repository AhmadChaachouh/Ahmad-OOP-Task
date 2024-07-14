from robots.base_robot import BaseRobot

class CleaningRobot(BaseRobot):
    def __init__(self, name: str, battery_level: int, status: str, cleaning_tool:str) -> None:
        super().__init__(name, battery_level, status)
        self.cleaning_tool = cleaning_tool


    def work(self):
        if self.battery_level > 20:
            print("Cleaning....")
            self.battery_level -= 20
        else:
            print("Can't clean, battery too low!")
    



