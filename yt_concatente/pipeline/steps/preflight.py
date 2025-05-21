from pipeline.steps.step import Step
from utils import Utils


class Preflight(Step):
    def process(self, data: list, inputs: dict, utils: Utils):
        self.logger.info('In preflight')
        utils.create_dir()
