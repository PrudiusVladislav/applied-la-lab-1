import numpy as np
import cv2 as cv
from plots import plot_objects, plot_object_3d
from transformations import (
    rotate_object,
    scale_object,
    reflect_object,
    shear_object,
    transform_object,
    rotate_object_3d,
    scale_object_3d)


def transform_3d_object(obj):
    plot_object_3d(obj, "Initial 3d object")
    rotated_obj = rotate_object_3d(obj, 45)
    scale_object_3d(rotated_obj, 2)


def transform_2d_objects(obj1, obj2, name1, name2):
    plot_objects(obj1, obj2, "Two initial 2d objects", name1, name2)

    rotate_object(obj1, 45)
    scale_object(obj2, 2)
    reflect_object(obj1, 'x')
    shear_object(obj2, 0.5, 'y')

    # transform obj1 with custom matrix (expanding x-axis by factor 0.5)
    custom_matrix = np.array([[0.5, 0], [0, 1]])
    transform_object(obj1, custom_matrix)


def transform_image(file_path):
    image = cv.imread(file_path)

    # Create rotation matrix
    center = (image.shape[1] // 2, image.shape[0] // 2)
    angle = 45  # Rotate the image by 45 degrees
    scale = 1.0  # Keep the original scale
    rotation_matrix = cv.getRotationMatrix2D(center, angle, scale)

    # Apply rotation
    rotated_image = cv.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

    # Create scaling matrix
    scale_factor = 2.0  # Scale the image by a factor of 2
    scaling_matrix = np.array([[scale_factor, 0, 0], [0, scale_factor, 0]])

    # Apply scaling
    scaled_image = cv.warpAffine(image, scaling_matrix, (image.shape[1], image.shape[0]))

    # Create translation matrix
    translation_matrix = np.float32([[1, 0, 25], [0, 1, 50]])

    # Apply translation
    translated_image = cv.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

    # Display the original and transformed images
    cv.imshow('Original Image', image)
    cv.waitKey(0)
    cv.imshow('Rotated Image', rotated_image)
    cv.waitKey(0)
    cv.imshow('Scaled Image', scaled_image)
    cv.waitKey(0)
    cv.imshow('Translated Image', translated_image)
    cv.waitKey(0)
    cv.destroyAllWindows()