import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def square_crop(image_array, size=400):
    """
    Crops a square portion from the center of the image.
    Parameters:
        image_array (np.ndarray): Input image as NumPy array
        size (int): Size of the square region to crop
    Returns: np.ndarray: The cropped square portion of the image
    """
    # Get image dimensions
    height, width = image_array.shape[0], image_array.shape[1]

    # Find the center of the image
    y, x = height // 2, width // 2

    # Calculate half of the square size
    half_size = size // 2

    # Calculate slice coordinates ensuring they stay within image boundaries
    y_start = max(0, y - half_size)
    y_end = min(height, y + half_size)
    x_start = max(0, x - half_size)
    x_end = min(width, x + half_size)

    # Extract the square portion
    return image_array[y_start:y_end, x_start:x_end]


def extract_channel(image):
    """
    Extracts a single channel from an image if it's RGB.
    Parameters: image (np.ndarray): Input image as NumPy array
    Returns: np.ndarray: Single-channel image
    """
    # Check if the image is RGB (3 channels)
    if len(image.shape) == 3 and image.shape[2] == 3:
        # Take only the first channel
        return image[:, :, 0:1]
    return image


def transpose_image(image):
    """
    Transposes an image (switches rows and columns).
    Parameters: image (np.ndarray): Input image as NumPy array
    Returns: np.ndarray: Transposed image
    """
    # Check if the image is 3D with a single channel
    if len(image.shape) == 3 and image.shape[2] == 1:
        # Squeeze to remove the third dimension before transpose
        squeezed = np.squeeze(image)
        # Transpose and return
        return squeezed.T

    # For 2D images or other cases
    return image.transpose()

    # .T: Property that returns standard matrix transpose, reversing axes order
    # .transpose(): Method returning view with axes transposed (customizable)


def display_image(image):
    """
    Displays an image.
    Parameters: image (np.ndarray): Image to display
    """
    plt.figure(figsize=(4, 4))
    plt.title("Transposed Image")
    plt.imshow(image, cmap='gray')
    plt.tight_layout()
    plt.show()


def main():
    """
    Loads an image, crops a square part, extracts a single channel,
    transposes it, and displays the results.
    """
    try:
        # Step 1: Load the image
        image_array = ft_load("animal.jpeg")

        # Exit if loading was unsuccessful
        if image_array is None:
            return

        # Step 2: Crop a square part from the image
        cropped_image = square_crop(image_array)

        # Step 3: Extract a single channel if it's RGB
        single_channel = extract_channel(cropped_image)

        # Print shape and data after cropping/channel extraction
        print(f"The shape of image is: {single_channel.shape}")
        print(single_channel)

        # Step 4: Transpose the image
        transposed_image = transpose_image(single_channel)

        # Print shape and data after transpose
        print(f"New shape after Transpose: {transposed_image.shape}")
        print(transposed_image)

        # Step 5: Display only the transposed image
        display_image(transposed_image)

    except Exception as e:
        print(f"An error occurred in the program: {e}")


if __name__ == "__main__":
    main()
