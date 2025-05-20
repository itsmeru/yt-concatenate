from pipeline.steps.step import Step
from utils import Utils


class Postflight(Step):
    def process(self, data: list, inputs: dict, utils: Utils):
        print('In postflight')
