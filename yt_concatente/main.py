import click

from pipeline.pipeline import Pipeline
from pipeline.steps.preflight import Preflight
from pipeline.steps.get_vedio_list import GetVedioList
from pipeline.steps.initialize_yt import InitializeYt
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.steps.read_captions import ReadCaptions
from pipeline.steps.search import Search
from pipeline.steps.download_videos import DownloadVideos
from pipeline.steps.postflight import Postflight
from utils import Utils

CHANNEL_ID = "UC_mYaQAE6-71rjSN6CeCA-g"


@click.command()
@click.option('--channel_id', required=True, help='YouTube 頻道ID')
@click.option('--search_word', required=True, help='要尋找的關鍵字')
def main(channel_id: str, search_word: str):
    steps = [
        Preflight(),
        GetVedioList(),
        InitializeYt(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        Postflight(),
    ]

    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'problem',
    }

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
