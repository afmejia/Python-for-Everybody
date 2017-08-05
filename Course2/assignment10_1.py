file = 'mbox.txt'
try:
	fhandler = open(file)
except:
	print('File not found')

# Iterate over the lines and identify 'From lines'
senders = dict()
for line in fhandler:
	words = line.split()
	if len(words) > 0 and words[0] == 'From':
		# rememember the person who sends the message
		sender = words[1]
		senders[sender] = senders.get(sender, 0) + 1

# get items in a nice representation
lst = list()
for k, v in senders.items():
	lst.append((v,k))

# get person with most messages sent
lst.sort(reverse = True)
print(lst[0][1], lst[0][0])