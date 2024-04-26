import cv2
import numpy as np
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

def process_image(image_file, filter_type, kernel_size):
    """
    Processes an image using the specified filter and kernel size.

    Args:
        image_file: An InMemoryUploadedFile object containing the image data.
        filter_type: The type of filter to apply ('average' or 'median').
        kernel_size: The size of the filter kernel.

    Returns:
        An InMemoryUploadedFile object containing the processed image data,
        or None if an error occurs.
    """

    # Read the image from the InMemoryUploadedFile
    image_data = image_file.read()
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: Could not load image from {image_file}")
        return None

    # Apply the selected filter
    if filter_type == 'average':
        processed_image = custom_average_filter(img, kernel_size)
    elif filter_type == 'median':
        processed_image = custom_median_filter(img, kernel_size)
    else:
        print("Error: Invalid filter type. Choose 'average' or 'median'.")
        return None

    # Convert the processed image back to an InMemoryUploadedFile
    _, encoded_image = cv2.imencode('.png', processed_image)
    processed_image_file = InMemoryUploadedFile(
        BytesIO(encoded_image),
        field_name='image',
        name='processed_image.png',
        content_type='image/png',
        size=len(encoded_image),
        charset=None
    )

    return processed_image_file

def custom_average_filter(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
    return cv2.filter2D(image, -1, kernel)

def custom_median_filter(image, kernel_size):
    if not isinstance(image, np.ndarray):
        raise ValueError("Input image must be a NumPy array")

    if len(image.shape) != 2:
        raise ValueError("Input image must be grayscale")

    height, width = image.shape
    result = np.zeros_like(image)
    half_kernel = kernel_size // 2

    for y in range(half_kernel, height - half_kernel):
        for x in range(half_kernel, width - half_kernel):
            neighborhood = image[y - half_kernel:y + half_kernel + 1, x - half_kernel:x + half_kernel + 1]
            result[y, x] = np.median(neighborhood.flatten())

    return result