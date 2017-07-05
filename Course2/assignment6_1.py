# Get input
word = input('Enter a word: ')

# Traverse word backwards
index = 1
while index <= len(word):
    print(word[-index])
    index += 1
