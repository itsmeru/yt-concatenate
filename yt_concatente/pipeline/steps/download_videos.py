from typing import List
import yt_dlp

from utils import Utils
from model.youtube import Youtube
from pipeline.steps.step import Step
from settings import VEDIOS_DIR


class DownloadVideos(Step):
    def process(self, data: list, inputs: dict, utils: Utils) -> List[Youtube]:
        yt_set = set([found.yt for found in data])
        # for yt in yt_set:
        #     url = yt.url
        #     output_path = f'{VEDIOS_DIR}/{yt.id}.%(ext)s'
        #     ydl_opts = {
        #         'format': 'best',
        #         'outtmpl': output_path,
        #         'quiet': True,
        #         'no_warnings': False,
        #         'nooverwrites': True,
        #     }
        #     if utils.video_file_exist(yt):
        #         print(f'found existing video file for {url}, skipping')
        #         continue
        #     try:
        #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #             ydl.download([url])
        #         print(f"Successfully downloaded: {url}")
        #     except yt_dlp.utils.DownloadError as e:
        #         print(f"Error downloading {url}: {str(e)}")

        return data
