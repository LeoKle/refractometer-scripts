""" Easy visualization for 3D points to 2D projection 
using the normal vector of the plane and constructing 
two span vectors using a help vector to fix the 2D plane rotation"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_vectors_and_cross_product(normal_vector, help_vector):
    # Calculate the cross product
    cross_product = np.cross(help_vector, normal_vector)
    cross_product2 = np.cross(normal_vector, cross_product)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot the original vectors
    ax.quiver(
        0,
        0,
        0,
        normal_vector[0],
        normal_vector[1],
        normal_vector[2],
        color="r",
        label="Normal vector",
    )
    ax.quiver(
        0,
        0,
        0,
        help_vector[0],
        help_vector[1],
        help_vector[2],
        color="b",
        label="Help vector",
    )

    # Plot the cross product vector
    ax.quiver(
        0,
        0,
        0,
        cross_product[0],
        cross_product[1],
        cross_product[2],
        color="g",
        label="Cross Product",
    )

    ax.quiver(
        0,
        0,
        0,
        cross_product2[0],
        cross_product2[1],
        cross_product2[2],
        color="g",
        label="Cross Product 2",
    )

    # Setting the axes properties
    max_val = max(
        np.linalg.norm(normal_vector),
        np.linalg.norm(help_vector),
        np.linalg.norm(cross_product),
    )
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])

    # Labels and legend
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()

    # Title
    ax.set_title("Vectors and their Cross Product")

    # Show the plot
    plt.show()


# Example usage
nv = [1, 0, -0.5]
help_vector1 = [0, 0, 1]
plot_vectors_and_cross_product(nv, help_vector1)
