#!/usr/bin/env python3

import csv
import datetime
import requests
import operator

FILE_URL = "https://storage.googleapis.com/gwg-hol-assets/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def getSortedData():
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    reader = sorted(reader,key=operator.itemgetter(3), reverse=False)
    return reader

def get_same_or_newer(start_date, employees_data):
    list_employees = []
    for row in employees_data:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')        
        if row_date < start_date:
            continue
        if row_date >= start_date:
            employee = "{} {}".format(row[0], row[1])
            list_employees.append("Started on {}: {}".format(row_date.strftime("%b %d, %Y"), employee))
    return list_employees    

def list_newer(start_date, employees_data):
    if start_date < datetime.datetime.today():
        final_employees = get_same_or_newer(start_date, employees_data)

        for employee in final_employees:
            print(employee)

def main():
    start_date = get_start_date() # ask user for date information
    employee = getSortedData() # gets the file from server and sort it.
    list_newer(start_date, employee) #retrieve the result list

if __name__ == "__main__":
    main()
