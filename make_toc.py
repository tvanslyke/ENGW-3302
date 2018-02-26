from sys import stdin


for line in stdin:
	if line and line[0] == '#':
		line = line.strip()
		tokens = line.split()
		hashes = tokens[0]
		name = " ".join(tokens[1:])
		indent = (len(hashes) - 1) * '\t'
		print("{}* [{}]({})".format(indent, name, line))
