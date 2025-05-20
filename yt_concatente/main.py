from pipeline.pipeline import Pipeline
from pipeline.steps.preflight import Preflight
from pipeline.steps.get_vedio_list import GetVedioList
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.steps.read_captions import ReadCaptions
from pipeline.steps.postflight import Postflight
from utils import Utils

CHANNEL_ID = "UC_mYaQAE6-71rjSN6CeCA-g"


def main():
    steps = [
        Preflight(),
        GetVedioList(),
        DownloadCaptions(),
        ReadCaptions(),
        Postflight(),
    ]

    inputs = {
        'channel_id': CHANNEL_ID
    }

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
