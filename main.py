import cv2  # opencv2 package for python.
import pafy  # pafy allows us to read videos from youtube.
URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # URL to parse
play = pafy.new(URL).streams[-1]  # '-1' means read the lowest quality of video.
assert play is not None  # we want to make sure their is a input to read.
stream = cv2.VideoCapture(play.url)  # create a opencv video stream.
from torch import hub  # Hub contains other models like FasterRCNN
model = torch.hub.load( \
                      'ultralytics/yolov5', \
                      'yolov5s', \
                      pretrained=True)