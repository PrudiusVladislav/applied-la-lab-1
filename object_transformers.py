import numpy as np
import cv2 as cv
from plots import plot_objects, plot_object_3d
from transformations_3d import rotate_object_3d, scale_object_3d
import transformations as tf
import transformations_open_cv as tf_cv


def transform_3d_object(obj):
    plot_object_3d(obj, "Initial 3d object")
    rotated_obj = rotate_object_3d(obj, 45)
    scale_object_3d(rotated_obj, 2)


def transform_2d_objects(obj1, obj2, name1, name2):
    plot_objects(obj1, obj2, "Two initial 2d objects", name1, name2)

    tf.rotate_object(obj1, 45)
    tf.scale_object(obj2, 2)
    tf.reflect_object(obj1, 'x')
    tf.shear_object(obj2, 0.5, 'y')

    # transform obj1 with custom matrix (expanding x-axis by factor 0.5)
    custom_matrix = np.array([[0.5, 0], [0, 1]])
    tf.transform_object(obj1, custom_matrix)


def transform_2d_objects_cv(obj1, obj2, name1, name2):
    plot_objects(obj1, obj2, "Two initial 2d objects", name1, name2)

    tf_cv.rotate_object(obj1, 45)
    tf_cv.scale_object(obj2, 2)  # TODO: fix: scale, reflect, shear
    tf_cv.reflect_object(obj1, 'x')
    tf_cv.shear_object(obj2, 0.5, 'y')


def transform_image(file_path):
    image = cv.imread(file_path)

    # Rotate
    center = (image.shape[1] // 2, image.shape[0] // 2)
    angle = 45  # Rotate the image by 45 degrees
    scale = 1.0  # Keep the original scale
    rotation_matrix = cv.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

    # Scale
    scale_factor = 2.0
    scaling_matrix = np.array([[scale_factor, 0, 0], [0, scale_factor, 0]])
    scaled_image = cv.warpAffine(image, scaling_matrix, (image.shape[1], image.shape[0]))

    # Shear
    shear_matrix = np.array([[1, 0.5, 0], [0, 1, 0]])  # along the x-axis by a factor of 0.5
    sheared_image = cv.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))

    cv.imshow('Original Image', image)
    cv.waitKey(0)
    cv.imshow('Rotated Image', rotated_image)
    cv.waitKey(0)
    cv.imshow('Scaled Image', scaled_image)
    cv.waitKey(0)
    cv.imshow('Sheared Image', sheared_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
