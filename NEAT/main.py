import retro
import numpy as np
import cv2
import neat
import pickle

env = retro.make(game = "SonicTheHedgehog-Genesis", state = "GreenHillZone.Act1")
