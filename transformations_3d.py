import numpy as np
from plots import plot_object_3d


def rotate_object_3d(obj, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    rotated_obj = np.dot(obj, rotation_matrix)
    plot_object_3d(rotated_obj, f"Rotated Object by {angle} degrees")
    return rotated_obj


def scale_object_3d(obj, scale_factor):
    scaling_matrix = np.array([
        [scale_factor, 0, 0],
        [0, scale_factor, 0],
        [0, 0, scale_factor]
    ])
    scaled_obj = np.dot(obj, scaling_matrix)
    plot_object_3d(scaled_obj, f"Scaled Object by factor {scale_factor}")
    return scaled_obj
