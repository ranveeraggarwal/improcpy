import cv2
from improcpy.enhancement.toonify import toonify


def main():
    img = cv2.imread('test_image.jpg')
    toonify(img)


if __name__ == '__main__':
    main()
