from open_b_fit.estimator.utils import read_landmark_positions_2d


class BaseDataPostprocessor:
    def __init__(self):
        pass


class PostprocessPrediction(BaseDataPostprocessor):
    def __init__(self):
        super().__init__()

    @staticmethod
    def post_process(prediction_results, width, height):
        return read_landmark_positions_2d(prediction_results, width, height)
