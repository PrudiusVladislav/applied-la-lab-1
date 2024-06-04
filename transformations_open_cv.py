import cv2 as cv
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
    obj_dims = obj.shape[:2]
    scaled_dims = tuple([int(dim * scale_factor) for dim in obj_dims])
    scaled_obj = cv.resize(obj, scaled_dims)
    plot_objects(obj, scaled_obj,
                 f"Scaled Object by factor {scale_factor}",
                 "Original Object",
                 "Scaled Object")
    return scaled_obj


def reflect_object(obj, axis):
    if axis.lower() == 'x':
        reflected_obj = cv.flip(obj, 0)
    elif axis.lower() == 'y':
        reflected_obj = cv.flip(obj, 1)
    else:
        raise ValueError("Axis can only be 'x' or 'y'")
    plot_objects(obj, reflected_obj,
                 f"Reflected Object along {axis}-axis",
                 "Original Object",
                 "Reflected Object")
    return reflected_obj
