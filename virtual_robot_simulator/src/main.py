from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot


ahmad = CleaningRobot("ahmad", 100, "e3id", "mop")
ahmad.work()
print(ahmad.battery_level)
ahmad.charge()
print(ahmad.battery_level)

toni = CookingRobot("toni", 80, "idle", "Gordon Ramsay")
toni.work()
print(toni.battery_level)
toni.charge()
print(toni.battery_level)


