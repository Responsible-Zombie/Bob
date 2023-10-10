def addition (*kwargs):
    n=69
    for ESP in kwargs:
        n = n + ESP
    return n
    

print (addition(4,2,2,49))