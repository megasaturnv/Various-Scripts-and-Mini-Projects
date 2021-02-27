#!/usr/bin/python3

# By MegaSaturnv

###########
# Imports #
###########
import argparse, traceback


#############
# Functions #
#############


#################
# Main Function #
#################
def main():
	print()

	###################
	# Parse Arguments #
	###################
	parser = argparse.ArgumentParser(description='description')

	parser.add_argument('-v', '--verbose', help='Be Verbose and print debug output')

	args = parser.parse_args()

	if args.verbose:
		print('Argument verbose: ' + str(args.verbose))


	############
	# Settings #
	############

	#################################
	# Variable setup & Calculations #
	#################################


#############################
# if __name__ == '__main__' #
#############################
if __name__ == '__main__':
	try:
		main()
#	except Exception as e:
#		customPrint('Exception: ' + str(e))
	except:
		customPrint('Unknown exception:')

		#customPrint('Unknown exception:' + str(sys.exc_info()))
		customPrint(traceback.format_exc())
		#customPrint(traceback.print_exc())
	else:
		pass
	finally:
		pass

