"""measures the size difference of a matrix as JSON vs as JPEG"""

import numpy as np
import json
import cv2
import io
from PIL import Image
import sys


def generate_random_matrix(rows, cols):
    """Generate a random matrix with given dimensions."""
    return np.random.rand(rows, cols, 3) * 255


def matrix_to_json(matrix):
    """Convert the NumPy matrix to a JSON string."""
    return json.dumps(matrix.tolist())


def matrix_to_jpeg(matrix):
    """Convert the NumPy matrix to a JPEG binary."""
    matrix = matrix.astype(np.uint8)
    success, encoded_image = cv2.imencode(".jpeg", matrix)
    if not success:
        raise ValueError("Could not encode the image to JPEG format.")
    return encoded_image.tobytes()


def to_binary(matrix):
    binary = matrix.tobytes()
    return binary


def main():
    rows, cols = 2560, 2440  # Define the size of the matrix
    matrix = generate_random_matrix(rows, cols)

    # Convert to JSON
    json_data = matrix_to_json(matrix)
    json_size = sys.getsizeof(json_data)

    # Convert to JPEG
    jpeg_data = matrix_to_jpeg(matrix)
    jpeg_size = sys.getsizeof(jpeg_data)

    binary_data = to_binary(matrix)
    binary_size = sys.getsizeof(binary_data)

    # Print size comparison
    print(f"Size of JSON data: {json_size} bytes")
    print(f"Size of JPEG data: {jpeg_size} bytes")
    print(f"Size of JPEG data: {binary_size} bytes")

    # # Save JSON and JPEG to files for verification (optional)
    # with open("matrix.json", "w") as json_file:
    #     json_file.write(json_data)

    # with open("matrix.jpeg", "wb") as jpeg_file:
    #     jpeg_file.write(jpeg_data)


if __name__ == "__main__":
    main()
