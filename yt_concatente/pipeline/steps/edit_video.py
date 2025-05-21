from typing import Tuple
from moviepy import VideoFileClip, concatenate_videoclips
from utils import Utils
from pipeline.steps.step import Step


class EditVideo(Step):
    def process(self, data: list, inputs: dict, utils: Utils) -> None:
        self.logger.info('Start editting videos')

        clips = []
        for found in data:
            if not utils.video_file_exist(found.yt):
                continue

            video_path = found.yt.video_filepath
            start, end = self.parse_caption_time(found.time)
            video = VideoFileClip(video_path).subclipped(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time: str) -> Tuple[Tuple[int, int, float], Tuple[int, int, float]]:
        start, end = caption_time.split(' --> ')
        return self.parse_time_string(start), self.parse_time_string(end)

    def parse_time_string(self, time_str: str) -> Tuple[int, int, float]:
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms)/1000
