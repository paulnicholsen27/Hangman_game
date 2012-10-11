def getwordlist(file):
	f = open(file)
	wordlist = []
	for word in f:
		word = word[:-2]
		wordlist.append(word)
	return wordlist

file = 2of12.txt	
f = open(file)
new_dictionary = []
for word in f:
	if len(word) > 4 and len(word) < 11:
		new_dictionary.append(word)
	print new_dictionary