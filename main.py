import numpy as np
import object_transformers as ot


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

# transform 3d object
ot.transform_3d_object(cube)

# transform 2d objects
ot.transform_2d_objects(triangle, irregular_polygon,
                        "Triangle",
                        "Irregular Polygon")

# transform image
ot.transform_image("landscape.jpg")

# ot.transform_2d_objects_cv(triangle, irregular_polygon,
#                            "Triangle",
#                            "Irregular Polygon")

