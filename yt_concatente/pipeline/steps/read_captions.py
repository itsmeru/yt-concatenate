import os

from pipeline.steps.step import Step
from utils import Utils


class ReadCaptions(Step):
    def process(self, data: list, inputs: dict, utils: Utils):
        for url in data:
            if not utils.caption_file_exists(url):
                continue

            captions = {}
            with open(utils.get_caption_filepath(url), "r", encoding="utf-8") as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            print(captions)
            break
        return data
