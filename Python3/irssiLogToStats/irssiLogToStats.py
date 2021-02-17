#!/usr/bin/python3

# MegaSaturnv 2020-02-17

##################
# Basic Settings #
##################
inputIrssiLogFile = 'IRSSI_input.log'  # Path to the log file created by IRSSI
outputCsvFile     = 'IRSSI_Output.csv' # Path to the output file which gives a total of messages sent by each message per day

#####################
# Advanced Settings #
#####################
matchesUsername = re.compile('(?<=^\d\d:\d\d <).*?(?=>)') # Regex which matches the username
matchesDate = re.compile('^---.+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{2})[\s\d:]+(\d{4})') # Regex which matches "--- Day changed..." or "--- Log opened/closed..."

################
# Dictionaries #
################
resultsDictionary = {} # Where the total number of messages per day are stored. Layout is {date : [messages sent by user 1], [...by user 2], [...by user 3]}
usernameDictionary = {} # Usernames stored here in a dict so their name can be converted to an ID, which represents their position in the resultsDictionary's list above. Layout is {

monthNumber = { # Dict of Month names and their number (two digit string). Used to convert e.g. 'Feb' to '02'
	'Jan' : '01',
	'Feb' : '02',
	'Mar' : '03',
	'Apr' : '04',
	'May' : '05',
	'Jun' : '06',
	'Jul' : '07',
	'Aug' : '08',
	'Sep' : '09',
	'Oct' : '10',
	'Nov' : '11',
	'Dec' : '12',
}

###########
# Imports #
###########
import csv, re

#############
# Main Code #
#############
with open(inputIrssiLogFile, "r") as f:
	currentDate = '0000-00-00' # If messages are detected at the start before figuring out what day it is, they will be shown as being sent on this date

	line = f.readline() # Read the first line
	while line:
		if (matchesDate.search(line)): # If it's a date, parse it
			currentMonthName = matchesDate.search(line).group(1) # Month Name e.g. 'Feb' could be the first group
			currentDay = matchesDate.search(line).group(2) # Day number is second group
			currentYear = matchesDate.search(line).group(3) # Year is third group

			currentDate = currentYear + '-' + monthNumber[currentMonthName] + '-' + currentDay # Set the current date to yyyy-mm-dd. monthNumber[currentMonthName] converts the three letter month name to a number (two digit string)
			if not currentDate in resultsDictionary: # If the date doesn't already exist in resultsDictionary
				resultsDictionary[currentDate] = [] # Create the index with a blank list
				for i in range(0, len(usernameDictionary)): # Append 0s until the list is the same length as the amount of users
					resultsDictionary[currentDate].append(0)

		elif (matchesUsername.search(line)): # If it's a regular message, parse the username
			username = matchesUsername.search(line).group(0)
			if not username in usernameDictionary: # If the username doesn't already exist in usernameDictionary
				usernameDictionary[username] = len(usernameDictionary) # Create the index and assign an ID. The new ID will always equal the size of the dict

			if username in usernameDictionary: # If the username is in usernameDictionary

				if len(resultsDictionary[currentDate]) <= usernameDictionary[username]: # If the length of the list in resultsDictionary for the current date is less than the ID of the user in the message
					while len(resultsDictionary[currentDate]) <= usernameDictionary[username]: # While the length of the list in resultsDictionary is not long enough to put the ID of the user in the correct place
						resultsDictionary[currentDate].append(0) # Increase the size of the list by appending 0's until the ID of the user is put in the correct list position

				resultsDictionary[currentDate][usernameDictionary[username]] = resultsDictionary[currentDate][usernameDictionary[username]] + 1 # Increment the number of messages sent by this user on this day by 1

		line = f.readline() # Read the next line

# Debugging:
#print('usernameDictionary')
#print(len(usernameDictionary))
#print(usernameDictionary)
#print('=======================================================')
#print('resultsDictionary')
#print(len(resultsDictionary))
#print(resultsDictionary)

# Generate the first line of the CSV file which contains the field names
csvFieldnames = list(usernameDictionary)
csvFieldnames.insert(0,'Date')

# Create the .csv file
with open(outputCsvFile, 'w') as f:
	w = csv.writer(f)

	w.writerow(csvFieldnames) # Write the field names to the first line

	for key in resultsDictionary:
		row = [key] # First item in a row is the date
		row.extend(resultsDictionary[key]) # Add the other items (message totals) to the list

		w.writerow(row)
