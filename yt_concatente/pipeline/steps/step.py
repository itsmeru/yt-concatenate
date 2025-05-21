from abc import ABC, abstractmethod
import logging

from utils import Utils


class Step(ABC):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def process(self, data: list, inputs: dict, utils: Utils):
        pass


class StepException(Exception):
    pass
