#!/usr/bin/python3

# MegaSaturnv 2021-02-22

###########
# Imports #
###########
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import datetime, os, sys

############
# Settings #
############
FONT_COLOUR        = (255,255,255) #(66,134,244)
FONT               = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
TEXT_POSITION      = (10,10)
SNAPSHOT_QUALITY   = 80
CUSTOM_PREFIX_TEXT = ''
CUSTOM_SUFFIX_TEXT = ''

#################
# Main Function #
#################
def main():
	TimeStampText = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	TimeStampText = str(CUSTOM_PREFIX_TEXT) + TimeStampText + str(CUSTOM_SUFFIX_TEXT)
	imageFilepath = sys.argv[1]

	img = Image.open(imageFilepath)
	draw = ImageDraw.Draw(img)

	draw.text(TEXT_POSITION, TimeStampText, FONT_COLOUR, font=FONT)
	img.save(imageFilepath, format='JPEG', quality=SNAPSHOT_QUALITY)
	#img.close?

#############################
# if __name__ == '__main__' #
#############################
if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print('Exception: ' + str(e)) # traceback.format_exc()/traceback.print_exc() is another option but that requires an import
#		print('Abort. Kill all launcher and aces processes')
#		killProcessByName(LAUNCHER_PROCESS_NAME)
#		killProcessByName(WARTHUNDER_PROCESS_NAME)
	except:
		print('Unknown exception')
	finally:
		# Check launcher and aces processes have closed. If not, kill them
		if isProcessRunning(LAUNCHER_PROCESS_NAME):
			killProcessByName(LAUNCHER_PROCESS_NAME)

		if isProcessRunning(WARTHUNDER_PROCESS_NAME):
			killProcessByName(WARTHUNDER_PROCESS_NAME)

