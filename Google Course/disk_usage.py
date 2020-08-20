import shutil # disk utility
import psutil # cpu utility

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
	print("Error")
else:
	print("Everything is ok")


du = shutil.disk_usage("/")
print("free disk space {:.2f}%".format(du.free/du.total*100))

print("CPU percent " + str(psutil.cpu_percent(0.1)))