def volume(a,b,c):
    def area(a,b):
        return a*b 
    return c * area(a,b)

print(volume(5,7,9))