import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(image_array, zoom=200):
    """
    Calculates the coordinates for zooming and
    returns the zoomed portion of the image.
    Parameters:image_array (np.ndarray, zoom_size (int)
    Returns: np.ndarray: The zoomed portion of the image
    """
    # Get image dimensions
    height, width = image_array.shape[0], image_array.shape[1]

    # Find the center of the image
    y, x = height // 2, width // 2

    # Calculate slice coordinates ensuring boundaries
    y_start = max(0, y - zoom)
    y_end = min(height, y + zoom)
    x_start = max(0, x - zoom)
    x_end = min(width, x + zoom)

    # Extract and return the zoomed portion
    return image_array[y_start:y_end, x_start:x_end]


def extract_first_channel(image):
    """
    Extracts the first channel from an RGB image.
    Parameters: image (np.ndarray): Input RGB image
    Returns: np.ndarray: Single-channel image (first channel only)
    """
    # Check if the image is RGB (3 channels)
    if len(image.shape) == 3 and image.shape[2] == 3:
        # Convert to grayscale by taking only the first channel
        return image[:, :, 0:1]
    # Image is already grayscale or has a different format
    return image


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

    # Handle different image formats
    if len(zoomed.shape) == 3 and zoomed.shape[2] == 3:
        plt.imshow(zoomed)
    elif len(zoomed.shape) == 3 and zoomed.shape[2] == 1:
        # Single-channel 3D image
        plt.imshow(zoomed[:, :, 0], cmap='gray')
    else:
        # 2D image
        plt.imshow(zoomed, cmap='gray')

    plt.colorbar()

    # Show the image on screen
    plt.tight_layout()
    plt.show()


def main():
    try:
        # Step 1: Load the image
        image_array = ft_load("animal.jpeg")

        # Exit if loading was unsuccessful
        if image_array is None:
            return

        # Step 2: Apply zooming to image center
        zoomed = zoom_image(image_array)

        # Step 3: Extract the first channel
        zoomed_2d = extract_first_channel(zoomed)

        # Step 4: Print information about the zoomed image
        print(f"New shape after slicing: {zoomed_2d.shape}")
        print(zoomed_2d)

        # Step 5: Display images
        display_images(image_array, zoomed_2d)

    except Exception as e:
        print(f"New shape after slicing: {e}")


if __name__ == "__main__":
    main()
