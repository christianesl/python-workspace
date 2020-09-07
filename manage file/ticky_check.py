#!/usr/bin/env python3

import sys
import csv
import re #regex
import operator #to sort dictionaries

#dictionaries
error = {}
per_user = {}

#regex 
regex_error = r'ERROR(.*)\((.*)\)'
regex_info = r'\((.*)\)'

# retrieve data form syslog file
with open('syslog.log') as syslog:
	for row in syslog:
		row.strip()
		# add data to dictionaries
		if 'ERROR' in row: #ERROR			
			res = re.search(regex_error, row)
			error_type = res.group(1)
			error_type = error_type.strip()
			error_user = res.group(2)

			if(error_type in error):
				error[error_type] += 1
			else:
				error[error_type] = 1

			if error_user not in per_user:
				per_user[error_user] = [0,0]
			per_user[error_user][1] += 1

		if 'INFO' in row: # INFO
			res = re.search(regex_info, row)
			info_user = res.group(1)
			if info_user not in per_user:
				per_user[info_user] = [0,0]
			per_user[info_user][0] += 1

# write CSV files
row = []

with open('error_message.csv', 'w') as error_csv:
	writer = csv.writer(error_csv)
	row.append("Error")
	row.append("Count")
	writer.writerow(row)

	for key,value in sorted(error.items(), key=operator.itemgetter(1), reverse=True):
		row[0] = str(key)
		row[1] = str(value)
		writer.writerow(row)

with open('user_statistics.csv', 'w') as user_csv:
	writer = csv.writer(user_csv)
	row[0] = "Username"
	row[1] = "INFO"
	row.append("ERROR")
	writer.writerow(row)
	
	for key in sorted(per_user.keys()):
		row[0] = str(key)
		row[1] = str(per_user[key][0])
		row[2] = str(per_user[key][1])
		writer.writerow(row)
