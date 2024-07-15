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

    @battery_level.setter
    def battery_level(self, level: int) -> None:
        self._battery_level = max(0, min(100, level))

    @property
    def status(self) -> str:
        return self._status

    @abstractmethod
    def work(self) -> None:
        pass

    def charge(self) -> None:
        self._battery_level = 100
        self._status = "charging"

    def report_status(self) -> None:
        print(f"Robot {self._name}: Status = {self._status}, Battery Level = {self._battery_level}%")

    def self_diagnose(self) -> None:
        print(f"Robot {self._name} performing self-diagnosis.")
        if self._battery_level < 20:
            print(f"Warning: Low battery level ({self._battery_level}%).")
        else:
            print("All systems are normal.")
