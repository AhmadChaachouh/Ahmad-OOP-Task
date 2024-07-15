# src/robots/base_robot.py

from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name: str):
        self._name = name
        self._battery_level = 100
        self._status = "idle"

    @property
    def name(self) -> str:
        return self._name

    @property
    def battery_level(self) -> int:
        return self._battery_level

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        self._status = status

    def charge(self) -> None:
        self._battery_level = 100
        self._status = "charging"

    @abstractmethod
    def work(self) -> None:
        pass

    def report_status(self) -> None:
        print(f"Robot {self._name}: Status = {self._status}, Battery Level = {self._battery_level}%")
