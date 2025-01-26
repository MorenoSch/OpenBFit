import cv2


class BaseDataPreprocessor:
    def __init__(self):
        pass


class PreprocessPredictData(BaseDataPreprocessor):
    def __init__(self):
        super().__init__()

    def pre_process(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
