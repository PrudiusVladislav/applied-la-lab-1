import numpy as np
import object_transformers as ot

# define two objects
triangle = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])
batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
cube = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0],  # lower square
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 1],  # upper square
    [1, 0, 1], [1, 0, 0],
    [1, 1, 0], [1, 1, 1],
    [0, 1, 1], [0, 1, 0]
])

# transform 3d object
ot.transform_3d_object(cube)

# transform 2d objects (numpy & transformation matrices)
ot.transform_2d_objects(triangle, batman,
                        "Triangle",
                        "Batman")

# transform 2d objects using opencv
ot.transform_2d_objects_cv(triangle, batman,
                           "Triangle",
                           "Batman")

# transform image (opencv)
ot.transform_image("landscape.jpg")


