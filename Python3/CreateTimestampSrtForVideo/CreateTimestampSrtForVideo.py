#!/usr/bin/python3

# CreateTimestampSrtForVideo.py by MegaSaturnv

#Todo:
# * Decide between subprocess.Popen or subprocess.run or something else entirely
# * More error checking - try except
# * Test compatibility with Windows
# * Check for ffprobe before running
# * Implement a batch mode for processing all video files in a Folder? Or, just use find and -exec...

###########
# Imports #
###########
import argparse, os, time, subprocess, pathlib
from datetime import datetime
from datetime import timedelta



#############
# Functions #
#############
#os.path.getmtime(path) #Cross-platform way to get file modification time in Python. It returns the Unix timestamp of when the file was last modified.
#os.path.getctime('file_path') #To get file creation time but only on windows.
#os.stat(path).st_birthtime #To get file creation time on Mac and some Unix based systems.
#pathlib.Path('file_path').stat().st_mtime #Best cross-platform way to get file modification time in Python.
#pathlib.Path('file_path').stat().st_ctime #To get file creation time but only on windows and recent metadata change time on Unix

def getVideoCreationTime(filepath):
	return os.stat(filepath).st_birthtime

def getVideoCreationTimeFfprobe(filepath):
	command = ['ffprobe', '-show_format', '-pretty', '-loglevel', 'quiet', filepath]
	commandPopen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#print(filepath)
	out, err =  commandPopen.communicate()
	#print('==========output==========')
	#print(out)
	if err:
		print(err)
		raise Exception('Error parsing video creation time')
	ffprobeInfo = out.splitlines()
	return ffprobeInfo[14][18:37].decode('utf-8')

def getVideoLength(filepath):
	result = subprocess.run(["ffprobe", "-v", "error", "-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1", filepath],
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT
	)
	
	#return float(result.stdout)
	return int(float(result.stdout))



#################
# Main Function #
#################
def main():
	###################
	# Parse Arguments #
	###################
	parser = argparse.ArgumentParser(description='A python 3 script to generate an srt file containing the video\'s timestamp. Start time is parsed from the video\'s metadata. srt file will be placed in the same directory as the specified video file. Requires ffprobe')

	parser.add_argument('-v', '--verbose', help='Be Verbose and print debug output', action="store_true")
	parser.add_argument('-t', '--test', help='Test run. Don\'t actually create any srt file. Recommended to be used with -v', action="store_true")
	parser.add_argument('-s', '--override-start-time', help='Manually specify the start date and time of the video file. Format is iso8601 - e.g. 2022-08-18T19:23:57')
	parser.add_argument('-l', '--override-length', help='Manually specify the length of the video file. Length in seconds')
	parser.add_argument('file', help='Video file to generate an srt for')

	args = parser.parse_args()

	#if args.verbose:
	#	print('Argument verbose:  ' + str(args.verbose))

	if not args.file: #Fallback check, though argparse should handle it
		raise Exception('Error. No file specified. Get help with -h or --help')

	############
	# Settings #
	############

	#################################
	# Variable setup & Calculations #
	#################################
	folderPath = str(pathlib.Path(args.file))
	#head, tail = os.path.split('args.file')

	srtFilePath = os.path.splitext(args.file)[0] + '.srt'
	#srtFilePath = os.path.basename(args.file)) + '.srt'

	if args.verbose:
		print('folderPath:        ' + folderPath)
		print('srtFilePath:       ' + srtFilePath)

	###########
	# Program #
	###########
	videoCreationTime = ''
	videoLength = 0

	if args.override_start_time:
		videoCreationTime = args.override_start_time
	else:
		videoCreationTime = getVideoCreationTimeFfprobe(args.file)
	if args.verbose:
		print('videoCreationTime: ' + str(videoCreationTime))

	if args.override_length:
		videoLength = args.override_length
	else:
		videoLength = getVideoLength(args.file)
	if args.verbose:
		print('videoLength:       ' + str(videoLength))


	startActualDateTime = datetime.strptime(videoCreationTime, "%Y-%m-%dT%H:%M:%S")
	startVideoDateTime = datetime.min


	if not args.test:
		if os.path.isfile(srtFilePath):
			raise Exception('Error. File already exists at: ' + srtFilePath)
		else:
			if args.verbose:
				print('Creating srt...')

			with open(srtFilePath, 'w') as f:
				for i in range(0, videoLength):
					f.write(str(i+1) + '\n')
					f.write((startVideoDateTime + timedelta(seconds=i)).strftime('%H:%M:%S,000 --> '))
					f.write((startVideoDateTime + timedelta(seconds=i+1)).strftime('%H:%M:%S,000\n'))
					f.write((startActualDateTime + timedelta(seconds=i)).strftime('%Y-%m-%d %H:%M:%S\n\n'))

			if args.verbose:
				print('Finished writing srt')



#############################
# if __name__ == '__main__' #
#############################
if __name__ == '__main__':
	main()

#	try:
#		main()
#	except Exception as e:
#		...
