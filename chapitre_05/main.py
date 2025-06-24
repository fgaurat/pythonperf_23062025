from Test import Test
from RectangleSingleton import RectangleSingleton
from Rectangle import Rectangle

def main():
    # t = Test()
    # print(t.toto)
    # t()
    r = RectangleSingleton()
    r1 = RectangleSingleton()
    print(hex(id(r)))
    print(hex(id(r1)))

    print(r)
    print(r1)

    r.longueur = 12
    r.largeur = 2

    print(r)
    print(r1)
    print(50*'-')
    r = Rectangle(2,4)
    print(r)
    r1 = Rectangle(12,54)
    print(r1)
    print(hex(id(r)))
    print(hex(id(r1)))    


if __name__ == '__main__':
    main()