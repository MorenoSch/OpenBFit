class BaseDataPostprocessor:
    def __init__(self):
        pass


class PostprocessPrediction(BaseDataPostprocessor):
    def __init__(self):
        super().__init__()
        raise NotImplementedError

    def pre_process(self):
        raise NotImplementedError
