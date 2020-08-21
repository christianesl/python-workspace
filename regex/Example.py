import re
log = "this is a line in a log [12345] 2020-08-21 14:49"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])



