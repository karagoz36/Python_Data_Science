import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def display_image(array, title="Image"):
    """
    Displays an image with the given title.
    """
    plt.figure(figsize=(5, 5))
    plt.title(title)
    plt.imshow(array)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def validate_image(array, check_channels=True):
    """
    Validates the input array to ensure if it's suitable.
    """
    # Check if array is None
    if array is None:
        print("Error: Input array is None")
        return False

    # Check if array is at least 2D
    if len(array.shape) < 2:
        print("Error: Input array must be at least 2D")
        return False
    # Check if array has RGB channels if required
    if check_channels and (len(array.shape) < 3 or array.shape[2] < 3):
        print("Error: Input must be 3D with 3 channels for color operations")
        return False

    return True


def ft_invert(array):
    """
    Inverts the color of the image received. (255 - value)
    """
    # Validate input array (doesn't need to check channels)
    if not validate_image(array, check_channels=False):
        return None

    # Invert the colors (255 - pixel value)
    inverted = array. copy()
    inverted = 255 - inverted

    # Display the inverted image
    display_image(inverted, "Figure VIII.2: Invert")

    return inverted


def ft_red(array):
    """
    Emphasizes the red channel by setting green and blue channels to 0.
    """
    if not validate_image(array):
        return None

    red = array.copy()
    red[:, :, 1] = 0 # Green channel = 0
    red[:, :, 2] = 0 # Blue channel = 0

    display_image(red, "Figure VIII.3: Red")

    return red


def ft_green(array):
    """
    Emphasizes the green channel by setting red and blue channels to 0.
    """
    if not validate_image(array):
        return None

    # Set red and blue channels to 0 (keep only green)
    green = array.copy()
    green[:, :, 0] = 0  # Red channel = 0
    green[:, :, 2] = 0  # Blue channel = 0

    display_image(green, "Figure VIII.4: Green")
    return green


def ft_blue(array):
    """
    Emphasizes the blue channel by setting red and green channels to 0.
    """
    if not validate_image(array):
        return None

    # Set red and green channels to 0 (keep only blue)
    blue = array.copy()
    blue[:, :, 0] = 0  # Red channel = 0
    blue[:, :, 1] = 0  # Green channel = 0

    display_image(blue, "Figure VIII.5: Blue")

    return blue

def ft_grey(array):
    """
    Converts the image to grayscale by averaging the RGB channels.
    """
    if not validate_image(array):
        return None

    # Calculate average of R, G, B channels
    grey = array.copy()
    grey_channel = (grey[:, :, 0] / 3 + grey[:, :, 1] / 3 + grey[:, :, 2] / 3)

    # Set all channels to the averaged value
    for i in range(3):
        grey[:, :, i] = grey_channel

    display_image(grey, "Figure VIII.6: Grey")

    return grey


def main():
    """
    Test function to demonstrate the image filtering functions.
    """
    try:
        image_path = "landscape.jpg"
        array = ft_load(image_path)

        display_image(array, "Figure VIII.1: Original")
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
