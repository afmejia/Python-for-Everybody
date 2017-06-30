total = 0.0
count = 0
av = 0.0

while True:
    try:
        number = input('Enter a number: ')
        if number == "done":
            break
        else:
            count = count + 1
            total = total + float(number)
    except:
        print('Bad data')

if count == 0:
    print('No values entered.')
else:
    av = total / count
    print(total, count, av)
