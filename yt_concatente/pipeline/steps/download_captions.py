from typing import List
from yt_dlp import YoutubeDL
import os
import yt_dlp

from pipeline.steps.step import Step
from utils import Utils
from model.youtube import Youtube


class DownloadCaptions(Step):
    def process(self, data: list, inputs: dict, utils: Utils) -> List[Youtube]:
        count = 0
        for yt in data:
            count += 1
            if count == 100:
                break
            if utils.caption_file_exists(yt):
                print('found exits caption file')
                continue

            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitleslangs': ['en'],
                'skip_download': True,
                'format': 'best',
                'quiet': True,
            }

            try:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.extract_info(yt.url, download=True)
                    subtitle_files = [f for f in os.listdir() if f.endswith('.vtt')]

                    for vtt_file in subtitle_files:
                        srt_content = utils.convert_to_srt(vtt_file)
                        with open(yt.caption_filepath, 'w', encoding='utf-8') as f:
                            f.write(srt_content)
                        os.remove(vtt_file)

            except (KeyError, AttributeError, yt_dlp.utils.DownloadError) as e:
                if "Sign in to confirm your age" in str(e):
                    print(f'Age restriction error for {yt.url}')
                else:
                    print('Error when download caption url for', yt.url)
                continue
            except Exception as e:
                print(f"Error type: {type(e)}")
                print(f"Error message: {str(e)}")
                continue

        return data
