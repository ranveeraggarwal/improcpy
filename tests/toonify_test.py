import cv2
from improcpy.enhancement.toonify import toonify


def main():
    img = cv2.imread('test_image.jpg')
    try:
        toonify(img)
    except:
        assert False


if __name__ == '__main__':
    main()
