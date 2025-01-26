import matplotlib.pyplot as plt

from open_b_fit.estimator.model_postprocessing import PostprocessPrediction
from open_b_fit.estimator.model_preprocessing import PreprocessPredictData
from open_b_fit.estimator.pose_estimator import SidePoseEstimator

image = PreprocessPredictData().pre_process("./tests/test_img.jpg.webp")
h, w, _ = image.shape
prediction = SidePoseEstimator().predict(image)
joint_positions = PostprocessPrediction().post_process(prediction, w, h)


plt.imshow(image)
plt.scatter(joint_positions[:, 0], joint_positions[:, 1])
plt.show()
