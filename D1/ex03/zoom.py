import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def zoom_image(image_array, zoom_size=200):
    """
    Calculates the coordinates for zooming on the center of an image and
    returns the zoomed portion of the image.

    Parameters:
        image_array (np.ndarray): Input image as NumPy array
        zoom_size (int): Number of pixels to extend from center in each direction

    Returns:
        np.ndarray: The zoomed portion of the image
    """
    # Get image dimensions
    height, width = image_array.shape[0], image_array.shape[1]

    # Find the center of the image
    center_y, center_x = height // 2, width // 2

    # Calculate slice coordinates ensuring they stay within image boundaries
    y_start = max(0, center_y - zoom_size)
    y_end = min(height, center_y + zoom_size)
    x_start = max(0, center_x - zoom_size)
    x_end = min(width, center_x + zoom_size)

    # Extract and return the zoomed portion
    return image_array[y_start:y_end, x_start:x_end]

def convert_to_grayscale(image):
    """
    Converts an RGB image to grayscale by taking only the first channel.

    Parameters:
        image (np.ndarray): Input RGB image

    Returns:
        np.ndarray: Grayscale image
        str: Description of the conversion
    """
    # Check if the image is RGB (3 channels)
    if len(image.shape) == 3 and image.shape[2] == 3:
        # Convert to grayscale by taking only the first channel
        return image[:, :, 0:1], "Converted RGB to grayscale using first channel"
    else:
        # Image is already grayscale or has a different format
        return image, "Image was already in grayscale format"

def display_images(original, zoomed):
    """
    Displays the original and zoomed images side by side.

    Parameters:
        original (np.ndarray): Original image array
        zoomed (np.ndarray): Zoomed image array
    """
    # Create figure with two subplots
    plt.figure(figsize=(12, 6))

    # Display original image
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original)
    plt.colorbar()

    # Display zoomed image
    plt.subplot(1, 2, 2)
    plt.title("Zoomed Image")

    # Handle different image formats for display
    if len(zoomed.shape) == 3 and zoomed.shape[2] == 3:
        # RGB image
        plt.imshow(zoomed)
    elif len(zoomed.shape) == 3 and zoomed.shape[2] == 1:
        # Single-channel 3D image
        plt.imshow(zoomed[:, :, 0], cmap='gray')
    else:
        # 2D image
        plt.imshow(zoomed, cmap='gray')

    plt.colorbar()
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function that processes an image, zooms in, and displays results.
    """
    try:
        # Step 1: Load the image
        image_array = ft_load("animal.jpeg")

        # Exit if loading was unsuccessful
        if image_array is None:
            return

        # Step 2: Apply zooming to image center
        zoomed_image = zoom_image(image_array)

        # Step 4: Convert to grayscale
        zoomed_image_gray, conversion_message = convert_to_grayscale(zoomed_image)

        # Step 5: Print information about the zoomed image
        print(f"New shape after slicing: {zoomed_image_gray.shape}")
        print(zoomed_image_gray)
        print(f"Note: {conversion_message}")

        # Step 6: Display images
        display_images(image_array, zoomed_image_gray)

    except Exception as e:
        print(f"An error occurred in the program: {e}")

if __name__ == "__main__":
    main()
