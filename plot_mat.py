import scipy.io
import numpy as np
import matplotlib.pyplot as plt

mat = scipy.io.loadmat("NBK7_detsig_bild.mat")
print(sorted(mat.keys()))
matrix = np.array(mat["NBK7_371519_mean"])

normalized_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))

plt.imshow(normalized_matrix, cmap="viridis", interpolation="nearest")
plt.colorbar(label="Normalized Intensity")
plt.title("Normalized Matrix as Image")
plt.xlabel("Pixel X")
plt.ylabel("Pixel Y")
plt.savefig("image.png")
