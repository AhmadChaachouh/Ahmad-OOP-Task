from abc import ABC, abstractmethod

class BaseRobot(ABC):

    def __init__(self, name:str, battery_level:int, status:str) -> None:
        self.name = name
        self.battery_level = battery_level
        self.status = status

    '''Sets robot battery level to 100 if not already'''
    def charge(self) -> None:
        if self.battery_level == 100:
            print("Battery full!")
        else:
            self.battery_level = 100

    @abstractmethod
    def work(self):
        pass

    def report_status(self):
        print(self.status)



    


    



