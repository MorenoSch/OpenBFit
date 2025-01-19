class BasePoseEstimator:
    def __init__(self):
        pass


class SidePoseEstimator(BasePoseEstimator):
    def __init__(self):
        super().__init__()
        raise NotImplementedError

    def predict(self):
        raise NotImplementedError


class RearPoseEstimator(BasePoseEstimator):
    def __init__(self):
        super().__init__()
        raise NotImplementedError

    def predict(self):
        raise NotImplementedError
