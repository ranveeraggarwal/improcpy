import cv2
import numpy as np


def toonify(image, canny_threshold_lower=90, canny_threshold_upper=250):
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
    :param canny_threshold_lower: float
        lower threshold value for Canny Edge Detection algorithm
    :param canny_threshold_upper: float
        upper threshold value for Canny Edge Detection algorithm
    :return: image
        the function returns a cartoon version of the input image

    Authors
    -------
    Anmol Kagrecha (akagrecha@gmail.com)
    """

    blurred_image = cv2.medianBlur(image, 5)

    # Edge detection and improvement
    detected_edges = cv2.Canny(blurred_image, canny_threshold_lower, canny_threshold_upper)
    edges = cv2.bitwise_not(detected_edges)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Applying bilateral filter to reduce the details
    reduced_image = cv2.bilateralFilter(image, 5, 150, 150)

    # Color quantization

    # Color quantization uses machine learning.
    # The image array is broken to get BGR values and centroid values are applied to all pixels.
    # Finally the image is reconstructed with new values.
    split_image = reduced_image.reshape((-1, 3))
    split_image = np.float32(split_image)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = 8
    _, label, center = cv2.kmeans(data=split_image, K=k, criteria=criteria, attempts=10,
                                  flags=cv2.KMEANS_RANDOM_CENTERS, bestLabels=None)

    center = np.uint8(center)
    reconstructed_image = center[label.flatten()]
    reconstructed_image = reconstructed_image.reshape(image.shape)

    # Final image
    result = cv2.bitwise_and(reconstructed_image, edges)

    return result
