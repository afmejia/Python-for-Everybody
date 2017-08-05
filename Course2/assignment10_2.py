file = 'mbox.txt'
try:
	fhandler = open(file)
except:
	print('File not found')

# Iterate over the lines and identify 'From lines'
hours = dict()
for line in fhandler:
	words = line.split()
	if len(words) > 0 and words[0] == 'From':
		# get the hour spliting by ':'
		hour = words[5].split(':')[0]
		
		# count frequency of each hour
		hours[hour] = hours.get(hour, 0) + 1

# create a list of tuples (frequency, hour)
lst = list()
for hour, freq in hours.items():
	lst.append((hour, freq))

# sort the list
lst.sort()

for k, v in lst:
	print(k, v)