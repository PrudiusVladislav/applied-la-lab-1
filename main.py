import numpy as np
import matplotlib.pyplot as plt


def plot_object(obj, title=""):
    plt.figure()
    plt.fill(obj[:, 0], obj[:, 1], edgecolor='b', fill=False)
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_objects(obj1, obj2, main_title, title1="", title2=""):
    plt.figure()

    plt.subplot(1, 2, 1)
    plt.fill(obj1[:, 0], obj1[:, 1], edgecolor='b', fill=False)
    plt.title(title1)
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.fill(obj2[:, 0], obj2[:, 1], edgecolor='b', fill=False)
    plt.title(title2)
    plt.grid(True)

    plt.suptitle(main_title)
    plt.show()


def rotate_object(obj, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rotated_obj = np.dot(obj, rotation_matrix)
    plot_objects(obj, rotated_obj,
                 f"Rotated Object by {angle} degrees",
                 "Original Object",
                 "Rotated Object")
    return rotated_obj


def scale_object(obj, scale_factor):
    scaling_matrix = np.array([[scale_factor, 0], [0, scale_factor]])
    scaled_obj = np.dot(obj, scaling_matrix)
    plot_objects(obj, scaled_obj,
                 f"Scaled Object by factor {scale_factor}",
                 "Original Object",
                 "Scaled Object")
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


# Define two objects
triangle = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])
irregular_polygon = np.array([[0, 0], [1, 0.5], [1.5, 1], [1, 1.5], [0.5, 1], [0, 0]])

# Plot the objects
plot_objects(triangle, irregular_polygon, "Two initial objects", "Triangle", "Irregular Polygon")

# Rotate object1 by 45 degrees
rotated_triangle = rotate_object(triangle, 45)

# Scale object2 by factor 2
scaled_object2 = scale_object(irregular_polygon, 2)

# Reflect object1 along x-axis
reflected_object1 = reflect_object(triangle, 'x')

# Shear object2 along y-axis by factor 0.5
sheared_object2 = shear_object(irregular_polygon, 0.5, 'y')

# Transform object1 with custom matrix
custom_matrix = np.array([[2, 0], [0, 1]])
transformed_object1 = transform_object(triangle, custom_matrix)




