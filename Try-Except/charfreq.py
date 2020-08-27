def character_frequency(filename):
	""" counts frequency of character """

	# open file
	try:
		f = open(filename)
	except OSError:
		return None

	# process the file
	characters = {}
	for line in f:
		for char in line:
			characters[char] = characters.get(char,0) + 1 # java map.getOrDefault()
	f.close()
	return characters		