import cv2
import numpy as np


def toonify(image, canny_threshold_lower=90, canny_threshold_upper=250,
            median_blur_kernel_size=5, bilateral_filter_d=5,
            bilateral_filter_sigma_color=150, bilateral_filter_sigma_space=150,
            max_iterations=10, epsilon=1.0, number_of_clusters=8):
    """ Toonify converts an image into a cartoon version of it.
    The image looks like it has been sketched.

    Algorithm
    ---------
    1. Median Blur: it is applied to reduce salt and pepper noise in the image
    2. Canny Edge Detection: it is used to add edges in the final image
    3. Bilateral Filter: bilateral filter is applied to reduce the details in the image
    4. Color Quantization: the method reduces the number of colors and leads to clustering of colors
                            that give the desired color effect in the image

    Notes
    -----
    The default thresholds give better results for portrait images.
    The thresholds maintain a balance on the number of edges visible on a face.

    Function Signature
    ------------------
    :param image: filename
        image is the input for the function
    :param canny_threshold_lower: double
        lower threshold value for Canny Edge Detection algorithm
    :param canny_threshold_upper: double
        upper threshold value for Canny Edge Detection algorithm
    :param median_blur_kernel_size: int
        kernel size for median blur
    :param bilateral_filter_d: int
        Diameter of each pixel neighborhood used in bilateral filter
    :param bilateral_filter_sigma_color: double
        bilateral filter sigma in color space
    :param bilateral_filter_sigma_space: double
        bilateral filter sigma in coordinate space
    :param max_iterations: int
        maximum iterations for cv2.kmeans
    :param epsilon: double
        minimum accuracy for cv2.kmeans
    :param number_of_clusters: int
        number of clusters set by cv2.kmeans
    :return: image
        the function returns a cartoon version of the input image

    Authors
    -------
    Anmol Kagrecha (akagrecha@gmail.com)
    Ranveer Aggarwal (ranveeraggarwal@gmail.com)
    """
    image = cv2.imread(image)
    blurred_image = cv2.medianBlur(image, median_blur_kernel_size)

    # Edge detection and improvement
    detected_edges = cv2.Canny(blurred_image, canny_threshold_lower, canny_threshold_upper)
    edges = cv2.bitwise_not(detected_edges)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Applying bilateral filter to reduce the details
    reduced_image = cv2.bilateralFilter(image, bilateral_filter_d,
                                        bilateral_filter_sigma_color, bilateral_filter_sigma_space)

    # Color quantization

    # Color quantization uses machine learning.
    # The image array is broken to get BGR values and centroid values are applied to all pixels.
    # Finally the image is reconstructed with new values.
    split_image = reduced_image.reshape((-1, 3))
    split_image = np.float32(split_image)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, max_iterations, epsilon)
    _, label, center = cv2.kmeans(data=split_image, K=number_of_clusters, criteria=criteria, attempts=10,
                                  flags=cv2.KMEANS_RANDOM_CENTERS, bestLabels=None)

    center = np.uint8(center)
    reconstructed_image = center[label.flatten()]
    reconstructed_image = reconstructed_image.reshape(image.shape)

    # Final image
    result = cv2.bitwise_and(reconstructed_image, edges)

    return result
