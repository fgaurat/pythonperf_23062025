import sys
import math
def main():
    a = 1
    print(hex(id(a)))
    a = 2 
    print(hex(id(a)))
    b = 2
    print(hex(id(b)))


    print(sys.getrefcount(654765432567497867632987))
    e = 654765432567497867632987
    print(sys.getrefcount(654765432567497867632987))


    s = "toto"
    # s[0] = "J"
    s1 = s+"titi"
    print(s1)

    # s = "Toto"+2 Erreur
    s = "Toto"+str(2)
    print(s)
    s = "Toto"*2
    # s = "Toto"*math.pi
    print(s)


    print(50*'-')

    a = 2
    s = "toto"

if __name__ == '__main__':
    main()