import numpy as np
from plots import plot_objects, plot_object_3d
from transformations import (
    rotate_object,
    scale_object,
    reflect_object,
    shear_object,
    transform_object,
    rotate_object_3d,
    scale_object_3d)

# define two objects
triangle = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])
irregular_polygon = np.array([[0, 0], [1, 0.5], [1.5, 1], [1, 1.5], [0.5, 1], [0, 0]])
cube = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0],  # lower square
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 1],  # upper square
    [1, 0, 1], [1, 0, 0],
    [1, 1, 0], [1, 1, 1],
    [0, 1, 1], [0, 1, 0]
])

plot_object_3d(cube, "Initial Cube")

# rotate cube by 45 degrees
rotated_cube = rotate_object_3d(cube, 45)

# scale cube by factor 2
scaled_cube = scale_object_3d(rotated_cube, 2)

# plot the objects
plot_objects(triangle, irregular_polygon, "Two initial 2d objects", "Triangle", "Irregular Polygon")

# rotate triangle by 45 degrees
rotated_triangle = rotate_object(triangle, 45)

# scale polygon by factor 2
scaled_object2 = scale_object(irregular_polygon, 2)

# reflect triangle along x-axis
reflected_object1 = reflect_object(triangle, 'x')

# shear polygon along y-axis by factor 0.5
sheared_object2 = shear_object(irregular_polygon, 0.5, 'y')

# transform triangle with custom matrix (expanding x-axis by factor 2)
custom_matrix = np.array([[2, 0], [0, 1]])
transformed_object1 = transform_object(triangle, custom_matrix)




