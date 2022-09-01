#!/usr/bin/python3

# StarTimelapse.py by MegaSaturnv

###########
# Imports #
###########
import argparse, os, serial, time
from datetime import datetime
from datetime import timedelta
from goprocam import GoProCamera, constants


#############
# Functions #
#############


#################
# Main Function #
#################
def main():
	###################
	# Parse Arguments #
	###################
	parser = argparse.ArgumentParser(description='description')

	parser.add_argument('-v', '--verbose', help='Be Verbose and print debug output', action="store_true")

	args = parser.parse_args()

	if args.verbose:
		print('Argument verbose: ' + str(args.verbose))

	############
	# Settings #
	############

	#################################
	# Variable setup & Calculations #
	#################################

	###########
	# Program #
	###########

	running = True
	while running:
		#Stuff
		running=False

#############################
# if __name__ == '__main__' #
#############################
if __name__ == '__main__':
	main()

#	try:
#		main()
#	except Exception as e:
#		...

