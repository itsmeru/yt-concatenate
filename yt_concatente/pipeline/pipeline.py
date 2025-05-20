from pipeline.steps.step import StepException


class Pipeline:
    def __init__(self, steps: list):
        self.steps = steps

    def run(self, inputs: dict, utils: list):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print(f'Exception happend: {e}')
                break
