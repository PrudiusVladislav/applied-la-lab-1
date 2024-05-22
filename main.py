import numpy as np
import matplotlib.pyplot as plt


def plot_object(obj, title=""):
    plt.figure()
    plt.fill(obj[:, 0], obj[:, 1], edgecolor='b', fill=False)
    plt.title(title)
    plt.grid(True)
    plt.show()


def rotate_object(obj, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rotated_obj = np.dot(obj, rotation_matrix)
    plot_object(rotated_obj, f"Rotated Object by {angle} degrees")
    return rotated_obj


def scale_object(obj, scale_factor):
    scaling_matrix = np.array([[scale_factor, 0], [0, scale_factor]])
    scaled_obj = np.dot(obj, scaling_matrix)
    plot_object(scaled_obj, f"Scaled Object by factor {scale_factor}")
    return scaled_obj


def reflect_object(obj, axis):
    if axis.lower() == 'x':
        reflection_matrix = np.array([[1, 0], [0, -1]])
    elif axis.lower() == 'y':
        reflection_matrix = np.array([[-1, 0], [0, 1]])
    else:
        raise ValueError("Axis can only be 'x' or 'y'")
    reflected_obj = np.dot(obj, reflection_matrix)
    plot_object(reflected_obj, f"Reflected Object along {axis}-axis")
    return reflected_obj


def shear_object(obj, shear_factor, axis):
    if axis.lower() == 'x':
        shear_matrix = np.array([[1, shear_factor], [0, 1]])
    elif axis.lower() == 'y':
        shear_matrix = np.array([[1, 0], [shear_factor, 1]])
    else:
        raise ValueError("Axis can only be 'x' or 'y'")
    sheared_obj = np.dot(obj, shear_matrix)
    plot_object(sheared_obj, f"Sheared Object along {axis}-axis by factor {shear_factor}")
    return sheared_obj


def transform_object(obj, transformation_matrix):
    transformed_obj = np.dot(obj, transformation_matrix)
    plot_object(transformed_obj, "Transformed Object with custom matrix")
    return transformed_obj


# Define two objects
object1 = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])
object2 = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]])

# Plot the objects
plot_object(object1, "Object 1")
plot_object(object2, "Object 2")

# Rotate object1 by 45 degrees
rotated_object1 = rotate_object(object1, 45)

# Scale object2 by factor 2
scaled_object2 = scale_object(object2, 2)

# Reflect object1 along x-axis
reflected_object1 = reflect_object(object1, 'x')

# Shear object2 along y-axis by factor 0.5
sheared_object2 = shear_object(object2, 0.5, 'y')

# Transform object1 with custom matrix
custom_matrix = np.array([[2, 0], [0, 1]])
transformed_object1 = transform_object(object1, custom_matrix)




