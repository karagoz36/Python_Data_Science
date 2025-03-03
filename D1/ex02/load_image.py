import numpy as np
from PIL import Image
from typing import Any


def ft_load(path: str) -> Any:
    """
    Load an image from the given path, print its format and pixel data.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: The image represented as a NumPy array.
    """
    try:
        image = Image.open(path)

        image_array = np.asarray(image)

        print(f"The shape of image is: {image_array.shape}")

        return image_array

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Cannot open the image file.")


if __name__ == "__main__":
    img_array = ft_load("landscape.jpg")
    if img_array is not None:
        print(img_array)

    img_array = ft_load("nonexistent.jpg")

    img_array = ft_load("document.txt")
