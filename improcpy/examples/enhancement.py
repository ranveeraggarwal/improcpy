import cv2

from improcpy.enhancement.toonify import toonify

img = cv2.imread('filename.jpg')

if img is not None:
    cv2.namedWindow('result', cv2.WINDOW_NORMAL)
    cv2.imshow('result', toonify(img))
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()
else:
    print("Image Doesn't Exist")
