import cv2
import argparse

from enhancement.toonify import toonify
from enhancement.action_sequence_generation import action_sequence_generator

parser = argparse.ArgumentParser()
parser.add_argument("-v1", "--video_asg", help="input the path to the video "
                                           "which is to be used for action sequence generation")
parser.add_argument("-i1", "--img_toonify", help="input the path to the image which is to be toonified")

args = vars(parser.parse_args())

if args.get("video_asg"):
    cv2.namedWindow('result', cv2.WINDOW_NORMAL)
    cv2.imshow('result', action_sequence_generator(args["video_asg"]))
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

elif args.get("img_toonify"):
    cv2.namedWindow('result', cv2.WINDOW_NORMAL)
    cv2.imshow('result', toonify(args["img_toonify"]))
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

else:
    print "please input a valid path to a video or an image"
