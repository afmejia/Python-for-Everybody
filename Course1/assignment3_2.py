# Get data
try:
    hrs = raw_input("Enter Hours: ")
    h = float(hrs)
    rate = float(raw_input("Enter rate: "))
except:
    print 'Error, please enter numeric input'
    quit()

print rate, h
if h <= 40:
    pay = h * rate
else:
    pay = 40 * rate + (h - 40) * 1.5 * rate
print pay
