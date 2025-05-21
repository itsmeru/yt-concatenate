
from typing import List
from pipeline.steps.step import Step
from utils import Utils
from model.found import Found


class Search(Step):
    def process(self, data: list, inputs: dict, utils: Utils) -> List[Found]:
        self.logger.info('Start searching key word')

        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    found.append(Found(yt, caption, time))

        return found
