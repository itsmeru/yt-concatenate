from pipeline.step.get_vedio_list import GetVedioList
from pipeline.pipeline import Pipeline

CHANNEL_ID = "UC_mYaQAE6-71rjSN6CeCA-g"


def main():
    steps = [
        GetVedioList(),
    ]

    inputs = {
        'channel_id': CHANNEL_ID
    }

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
