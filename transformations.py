import numpy as np
from plots import plot_objects, plot_object_3d


def rotate_object(obj, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rotated_obj = np.dot(obj, rotation_matrix)
    plot_objects(obj, rotated_obj,
                 f"Rotated Object by {angle} degrees",
                 "Original Object",
                 "Rotated Object")
    return rotated_obj


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


def scale_object(obj, scale_factor):
    scaling_matrix = np.array([[scale_factor, 0], [0, scale_factor]])
    scaled_obj = np.dot(obj, scaling_matrix)
    plot_objects(obj, scaled_obj,
                 f"Scaled Object by factor {scale_factor}",
                 "Original Object",
                 "Scaled Object")
    return scaled_obj


def scale_object_3d(obj, scale_factor):
    scaling_matrix = np.array([
        [scale_factor, 0, 0],
        [0, scale_factor, 0],
        [0, 0, scale_factor]
    ])
    scaled_obj = np.dot(obj, scaling_matrix)
    plot_object_3d(scaled_obj, f"Scaled Object by factor {scale_factor}")
    return scaled_obj


def reflect_object(obj, axis):
    if axis.lower() == 'x':
        reflection_matrix = np.array([[1, 0], [0, -1]])
    elif axis.lower() == 'y':
        reflection_matrix = np.array([[-1, 0], [0, 1]])
    else:
        raise ValueError("Axis can only be 'x' or 'y'")
    reflected_obj = np.dot(obj, reflection_matrix)
    plot_objects(obj, reflected_obj,
                 f"Reflected Object along {axis}-axis",
                 "Original Object",
                 "Reflected Object")
    return reflected_obj


def shear_object(obj, shear_factor, axis):
    if axis.lower() == 'x':
        shear_matrix = np.array([[1, shear_factor], [0, 1]])
    elif axis.lower() == 'y':
        shear_matrix = np.array([[1, 0], [shear_factor, 1]])
    else:
        raise ValueError("Axis can only be 'x' or 'y'")
    sheared_obj = np.dot(obj, shear_matrix)
    plot_objects(obj, sheared_obj,
                 f"Sheared Object along {axis}-axis by factor {shear_factor}",
                 "Original Object",
                 "Sheared Object")
    return sheared_obj


def transform_object(obj, transformation_matrix):
    transformed_obj = np.dot(obj, transformation_matrix)
    plot_objects(obj, transformed_obj,
                 "Transformed Object with custom matrix",
                 "Original Object",
                 "Transformed Object")
    return transformed_obj
