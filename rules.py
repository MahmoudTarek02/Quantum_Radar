from abc import ABC, abstractmethod
from typing import Optional
from car_type import CarType
from observation import Observation
from violation import Violation

class Rule(ABC):
    @abstractmethod
    def evaluate(self, observation: Observation) -> Optional[Violation]:
        pass

class TruckSpeedRule(Rule):
    def evaluate(self, observation: Observation) -> Optional[Violation]:
        if observation.car_type == CarType.TRUCK and observation.speed > 60:
            return Violation(
                rule_name=self.__class__.__name__,
                description=f"speed of {int(observation.speed)} exceeded max alLowed 60",
                fine_amount=300
            )
        return None

class PrivateSpeedRule(Rule):
    def evaluate(self, observation: Observation) -> Optional[Violation]:
        if observation.car_type == CarType.PRIVATE and observation.speed > 80:
            return Violation(
                rule_name=self.__class__.__name__,
                description=f"speed of {int(observation.speed)} exceeded max alLowed 80",
                fine_amount=300
            )
        return None

class SeatbeltRule(Rule):
    def evaluate(self, observation: Observation) -> Optional[Violation]:
        if observation.car_type == CarType.PRIVATE and not observation.seatbelt_fastened:
            return Violation(
                rule_name=self.__class__.__name__,
                description="Seatbelt not fastned",
                fine_amount=100
            )
        return None
