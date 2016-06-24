import cv2


def action_sequence_generator(video, frames_required=8, thresh=35, maxval=255):

    """
    Action Sequence Generator converts a video containing an action sequence
    into an image having various foreground positions superimposed on the background.

    Algorithm
    _________
    1. Algorithm chooses the required frames in the video and compares it with the first frame
        to generate the foreground mask.
    2. Foreground mask is used to get the foreground from the frame while the background mask
        is applied on the first frame.
    3. The foreground is added to modified first frame. The required number of frames are looped
        to generate the result.

    Notes
    _____
    The algorithm works best when the first frame contains only the background.
    Thresholds to generate the foreground mask have to manipulated to get the desired results.

    Function Signature
    __________________
    :param video: filename
           video is the input for the function
    :param frames_required: int
           number of frames to be considered to generate the result
    :param thresh: double
           threshold value for cv2.threshold
    :param maxval: double
           maximum value to be used for cv2.threshold

    Authors
    _______
    Anmol Kagrecha
    Ranveer Aggarwal

    """
    cap = cv2.VideoCapture(video)
    # frame numbers according to chosen number of frames
    number_of_frames = int(cap.get(7))
    frame_numbers = [i for i in range(0, number_of_frames - 1, int((number_of_frames - 1) / frames_required))]

    # list to store the frames
    video_frames = []

    while 1:
        ret, frame = cap.read()

        if ret == 0:
            break

        video_frames.append(frame)

    cap.release()

    # referencing the first frame for further analysis
    first_frame = cv2.cvtColor(video_frames[0], cv2.COLOR_BGR2GRAY)
    result = video_frames[0]

    for i in frame_numbers:
        if i == 0:
            continue

        frame = video_frames[i]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_delta = cv2.absdiff(gray, first_frame)

        # generating the foreground and background masks
        foreground_mask = cv2.threshold(frame_delta, thresh, maxval, 0)[1]
        background_mask = cv2.bitwise_not(foreground_mask)

        # foreground generation
        foreground = cv2.bitwise_and(frame, frame, mask=foreground_mask)

        # final recombination to generate the result
        result = cv2.bitwise_and(result, result, mask=background_mask)
        result = cv2.add(result, foreground)

    return result
