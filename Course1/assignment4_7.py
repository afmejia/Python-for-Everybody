def computegrade(score):
    if score > 1.0:
        print 'Invalid value'
    elif score >= 0.9:
        print 'A'
    elif score >= 0.8:
        print 'B'
    elif score >= 0.7:
        print 'C'
    elif score >= 0.6:
        print 'D'
    elif score >= 0.0:
        print 'F'
    else:
        print 'Invalid value'

try:
    score = float(raw_input("Enter a value between 0.0 and 1.0: "))
except:
    print 'Not valid value'
    quit()

computegrade(score)
