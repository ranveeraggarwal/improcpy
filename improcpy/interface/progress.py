import sys


def update_progress(progress):
    """
    Displays or updates a console progress bar
    Accepts a float between 0 and 1. Any int will be converted to a float.
    A value under 0 represents a 'halt'.
    A value at 1 or bigger represents 100%

    Function Signature
    ------------------
    :param progress: float
    :return:

    Authors
    -------
    Ranveer Aggarwal

    """
    bar_length = 100  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "Error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt!\r\n"
    if progress >= 1:
        progress = 1
        status = "Completed!\r\n"
    block = int(round(bar_length*progress))
    text = "\rProgress: [{0}] {1}% {2}".format("#"*block + "-"*(bar_length-block), int(progress*100), status)
    sys.stdout.write(text)
    sys.stdout.flush()
