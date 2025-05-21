from typing import List
from pipeline.steps.step import Step
from model.youtube import Youtube
from utils import Utils


class InitializeYt(Step):
    def process(self, data: list, inputs: dict, utils: Utils) -> List[Youtube]:
        return [Youtube(url) for url in data]
