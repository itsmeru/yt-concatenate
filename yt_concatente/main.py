import click

from pipeline.pipeline import Pipeline
from pipeline.steps.preflight import Preflight
from pipeline.steps.get_vedio_list import GetVedioList
from pipeline.steps.initialize_yt import InitializeYt
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.steps.read_captions import ReadCaptions
from pipeline.steps.search import Search
from pipeline.steps.download_videos import DownloadVideos
from pipeline.steps.edit_video import EditVideo
from pipeline.steps.postflight import Postflight
from utils import Utils


@click.command()
@click.option('-c', '--channel_id', type=str, required=True, help='YouTube 頻道ID')
@click.option('-w', '--search_word', type=str, required=True, help='要尋找的關鍵字')
def main(channel_id: str, search_word: str):
    steps = [
        Preflight(),
        GetVedioList(),
        InitializeYt(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    inputs = {
        'channel_id': channel_id,
        'search_word': search_word,
        'vedio_limit': 100,
        'limit': 20,
        'cleanup': True,
    }

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
