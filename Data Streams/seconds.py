def to_seconds(hour, minute, second):
	return hour*3600+minute*60+second

print("Welcome to this converter")

cont = "y"

while(cont.lower() == "y"):
	hours = int(input("Enter hour: "))
	minutes =int(input("Enter minutes: "))
	seconds = int(input("Enter seconds: "))

	print("Result {} seconds.".format(to_seconds(hours, minutes, seconds)))
	print()
	cont = input("Continue? [y to continue]")

print("End")