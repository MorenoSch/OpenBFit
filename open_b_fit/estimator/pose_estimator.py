import mediapipe as mp


class BasePoseEstimator:
    def __init__(self):
        pass


class SidePoseEstimator(BasePoseEstimator):
    def __init__(self):
        super().__init__()
        self.model = mp.solutions.pose.Pose(static_image_mode=True)

    def predict(self, image):
        results = self.model.process(image)
        return results
