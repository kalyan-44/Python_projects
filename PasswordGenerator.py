import random
def passwordGenerator():
    # Write your code here #
    #password = "sample"
    a = ['&','!','*']
    b = ['A','B','C','D','E']
    c = ['a','b','c','d','e']
    d = ['1''2','3','4','5']
    password = random.choice(a) + random.choice(b) + random.choice(c) + random.choice(d)
    password = password + password
    return password