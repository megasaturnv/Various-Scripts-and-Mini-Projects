#!/usr/bin/python3
from goprocam import GoProCamera, constants

import time

goprocamera = GoProCamera.GoPro()
#goprocamera = GoProCamera.GoPro(constants.auth)

goprocamera.overview()
goprocamera.listMedia(True)
