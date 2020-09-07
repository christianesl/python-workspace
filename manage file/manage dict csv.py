import csv

#reading from the csv
with open('software.csv') as software:
	reader = csv.DictReader(software)
	for row in reader:
		print(("{} has {} users").format(row["name"], row["users"]))

#writing to the csv
users [ {"name":"name1", "username": "username1", "department": "deparment1"},
		{"name":"name2", "username": "username2", "department": "deparment2"},
		{"name":"name3", "username": "username3", "department": "deparment3"}]

keys = ["name", "username", "deparment"]
with open('by_department.csv', 'w') as by_department:
	writer = csv.DictWriter(by_department, fieldnames=keys)
	writer.writeheader()
	
	writer.writerows(users)