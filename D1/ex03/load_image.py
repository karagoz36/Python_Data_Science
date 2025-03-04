import numpy as np
from PIL import Image
import os

def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path, print its format and pixel data.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: The image represented as a NumPy array.
    """
    try:
        # Load the image
        image = Image.open(path)

        # Convert to NumPy array
        array = np.array(image)

        # Print the image dimensions
        print(f"The shape of image is: {array.shape}")

        # Print the pixel content
        print(array)

        return array

    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except IOError:
        print("Error: Cannot open the image file.")
        return None
