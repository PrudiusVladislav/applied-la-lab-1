import cv2 as cv
import numpy as np
from plots import plot_objects


def rotate_object(obj, angle):
    center = (obj.shape[1] // 2, obj.shape[0] // 2)
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated_obj = cv.warpAffine(obj, rotation_matrix, (obj.shape[1], obj.shape[0]))
    plot_objects(obj, rotated_obj,
                 f"Rotated Object by {angle} degrees",
                 "Original Object",
                 "Rotated Object")
    return rotated_obj


def scale_object(obj, scale_factor):
    scaling_matrix = np.array([[scale_factor, 0, 0], [0, scale_factor, 0]])
    scaled_obj = cv.warpAffine(obj, scaling_matrix, (int(obj.shape[1]*scale_factor), int(obj.shape[0]*scale_factor)))
    plot_objects(obj, scaled_obj,
                 f"Scaled Object by factor {scale_factor}",
                 "Original Object",
                 "Scaled Object")
    return scaled_obj


def reflect_object(obj, axis):
    if axis.lower() == 'x':
        reflection_matrix = cv.flip(obj, 0)
    elif axis.lower() == 'y':
        reflection_matrix = cv.flip(obj, 1)
    else:
        raise ValueError("Axis can only be 'x' or 'y'")
    reflected_obj = cv.warpAffine(obj, reflection_matrix, (obj.shape[1], obj.shape[0]))
    plot_objects(obj, reflected_obj,
                 f"Reflected Object along {axis}-axis",
                 "Original Object",
                 "Reflected Object")
    return reflected_obj


def shear_object(obj, shear_factor, axis):
    rows, cols = obj.shape[:2]
    if axis.lower() == 'x':
        shear_matrix = np.float32([[1, shear_factor, 0], [0, 1, 0]])
    elif axis.lower() == 'y':
        shear_matrix = np.float32([[1, 0, 0], [shear_factor, 1, 0]])
    else:
        raise ValueError("Axis can only be 'x' or 'y'")
    sheared_obj = cv.warpAffine(obj, shear_matrix, (cols, rows))
    plot_objects(obj, sheared_obj,
                 f"Sheared Object along {axis}-axis by factor {shear_factor}",
                 "Original Object",
                 "Sheared Object")
    return sheared_obj




