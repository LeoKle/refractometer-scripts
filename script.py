import os
import math
import numpy as np
import matplotlib.pyplot as plt

NANOMETERS = 1e-9
b = (1.03961212, 0.231792344, 1.01046945)
c = (0.00600069867, 0.020017944, 103.560653)


def sellmeier_equation(b, c, wavelength):
    wavelength_squared = (wavelength / 1e-6) ** 2

    term_sum = 0.0
    for n in range(len(b)):
        term_sum += (b[n] * wavelength_squared) / (wavelength_squared - c[n])

    n_squared = 1 + term_sum
    return math.sqrt(n_squared)


def plot(wavelengths, refractive_indices, filename):
    plt.figure()
    plt.plot(np.array(wavelengths) / NANOMETERS, refractive_indices)
    plt.grid(True)
    plt.ylim(min(refractive_indices) * 0.999, max(refractive_indices) * 1.001)
    plt.savefig(filename.strip(".txt") + ".png")


def read_txt_files(directory):
    files = os.listdir(directory)

    # Filter out all non-txt files
    txt_files = [f for f in files if f.endswith(".txt")]

    # Read and process each txt file
    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        try:
            with open(file_path, "r") as file:
                content = file.read()
                print(f"Reading file: {txt_file}")

                wavelengths_str, _ = content.split("\n\n")

                wavelengths = [
                    int(wl_str) * NANOMETERS for wl_str in wavelengths_str.split(";")
                ]

                refractive_indices = [
                    sellmeier_equation(b, c, wl) for wl in wavelengths
                ]

                plot(wavelengths, refractive_indices, file_path)

        except Exception as e:
            print(f"Error reading file {txt_file}: {e}")


directory = "data"
read_txt_files(directory)
