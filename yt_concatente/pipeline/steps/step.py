from abc import ABC, abstractmethod

from utils import Utils


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data: list, inputs: dict, utils: Utils):
        pass


class StepException(Exception):
    pass
