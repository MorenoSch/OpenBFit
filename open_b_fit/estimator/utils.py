from typing import Any

import mediapipe as mp
import numpy as np
import numpy.typing as npt


def read_landmark_positions_3d(
    results: Any,
) -> npt.NDArray[np.float32] | None:
    if results.pose_landmarks is None:
        return None
    else:
        # Extract 3D landmark positions
        landmarks = [
            results.pose_world_landmarks.landmark[lm]
            for lm in mp.solutions.pose.PoseLandmark
        ]
        return np.array([(lm.x, lm.y, lm.z) for lm in landmarks])


def read_landmark_positions_2d(
    results: Any,
    image_width: int,
    image_height: int,
) -> npt.NDArray[np.float32] | None:
    if results.pose_landmarks is None:
        return None
    else:
        normalized_landmarks = [
            results.pose_landmarks.landmark[lm] for lm in mp.solutions.pose.PoseLandmark
        ]
        return np.array(
            [(image_width * lm.x, image_height * lm.y) for lm in normalized_landmarks]
        )
