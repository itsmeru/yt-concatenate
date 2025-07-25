from typing import List
from pipeline.steps.step import Step
from utils import Utils
from model.youtube import Youtube


class ReadCaptions(Step):
    def process(self, data: list, inputs: dict, utils: Utils) -> List[Youtube]:
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open(yt.caption_filepath, "r", encoding="utf-8") as f:
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
            yt.captions = captions

        return data
