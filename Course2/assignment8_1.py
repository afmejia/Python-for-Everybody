def chop(t):
    # Delete first element
    del t[0]

    # Delete last element
    t.pop()

def middle(t):
    return t[1:len(t) - 1]

t = ['java', 'php', 'python', 'c++', 'c', 'ruby']
t2 = middle(t)
print(t)
print(t2)
