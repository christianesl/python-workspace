import csv

dict1 = {'error_type': 6, 'error_type2': 12}
row = []

with open('tmp.csv', 'w') as error_csv:
	writer = csv.writer(error_csv)
	row.append("Error")
	row.append("Count")
	writer.writerow(row)
	
	for key in dict1.keys():		
		row[0] = str(key)		
		row[1] = str(dict1[key])
		writer.writerow(row)