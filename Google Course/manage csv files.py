#reading csv
import csv
f = open("csv_file.txt")
cvf_f = csv.reader(f)
for row in csv_f:
	name, phone, role = row
	print( "Name: {} Phone:{} Department:{}".format(name,phone, role))

#writing to csv
hosts = [["workstation.local", "192.168.25.56"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
	writer = csv.writer(hosts.csv)
	writer.writerows(hosts) #writerow for single data
	