import cv2
import numpy as np


def toonify(_image, _canny_threshold_lower=90, _canny_threshold_upper=250):

    """
    toonify converts an image into a cartoonized version of it.
    The image looks like it has been sketched.

    The function uses a few algorithms:
        1. median blur -> it is applied to reduce salt and pepper noise in the image
        2. canny edge detection -> it is used to add edges in the final image
        3. bilateral filter -> bilateral filter is applied to reduce the details in the image
        4. color quantization -> the method reduces the number of colors and leads to clustering of colors
                                that give the desired color effect in the image
    :param
        1. _image -> _image is the input for the function
        2. _canny_threshold_lower -> lower threshold value for Canny Edge Detection algorithm
        3. _canny_threshold_upper -> upper threshold value for Canny Edge Detection algorithm
        Note- The default thresholds give better results for portrait images.
        ...The thresholds maintain a balance on the number of edges visible on a face.

    :return:
    the function returns a tooned version of the input image

    :AUTHOR:
    Anmol Kagrecha (akagrecha@gmail.com)
    in MENTORSHIP of
    Ranveer Aggarwal (ranveeraggarwal@gmail.com)
    """

    if _image.size is None:
        return "image does not exist"

    else:
        _image_copy = _image.copy()

        _image = cv2.medianBlur(_image, 5)

        # edge detection and improvement
        _edges = cv2.Canny(_image, _canny_threshold_lower, _canny_threshold_upper)
        _edges = cv2.bitwise_not(_edges)
        _edges = cv2.cvtColor(_edges, cv2.COLOR_GRAY2BGR)

        # applying bilateral filter to reduce the details
        _image_copy = cv2.bilateralFilter(_image_copy, 5, 150, 150)

        # color quantization
        """
        Color quantization uses machine learning.
        The image array is broken to get BGR values and centroid values are applied to all pixels.
        Finally the image is reconstructed with new values.
        """
        _image_split = _image_copy.reshape((-1, 3))
        _image_split = np.float32(_image_split)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        k = 8
        _ret, _label, _center = cv2.kmeans(_image_split, k, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        _center = np.uint8(_center)
        _res = _center[_label.flatten()]
        _res2 = _res.reshape(img.shape)

        # final _image
        _result = cv2.bitwise_and(_res2, _edges)

        return _result

img = cv2.imread('filename.jpg')

cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('result', toonify(img))
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

