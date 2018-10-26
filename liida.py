from sys import argv
script, a, b, c = argv

a = int(a)
b = int(b)
c = int(c)

def funktsioon(a, b, c):
    print ((a+b)*c)
    
funktsioon(a,b,c)

funktsioon(c,b,a)