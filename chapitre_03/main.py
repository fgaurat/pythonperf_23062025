from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    # r = Rectangle(longueur=2,largeur=3)
    
    r = Rectangle(12,3)
    r3 = Rectangle(12,3)
    
    r1 = DataRectangle(12,3)
    r2 = DataRectangle(12,3)
    
    print(r1,id(r1))
    print(r2,id(r2))

    if r1==r2:
        print("ok")
    else:
        print("ko")



    print(f"{r1.longueur=}")
    print(f"{r1.largeur=}")
    r1.longueur =  54
    r1.largeur =  23
    print(f"{r1.longueur=}")
    print(f"{r1.largeur=}")
    print(f"{r1.surface=}")


    print(f"{r.longueur=}")
    print(f"{r.largeur=}")

    
    r.longueur = 87
    
    print(r.longueur)
    print(r.largeur)
    print(r.surface)

    print(50*'-')
    r = Rectangle(12,3)
    r1 = Rectangle(32,5)
    
    print(r.get_cpt())
    print(r1.get_cpt())
    print(Rectangle.get_cpt())
    
    r = Rectangle()
    r = Rectangle(longueur=12)
    r = Rectangle(largeur=12)
    r = Rectangle.build_from_str("12;4")
    print(r.longueur)
    print(r.largeur)

    r = Rectangle()
    # r.longeur = 34
    print(r.longueur)
    print(r.largeur)
    # print(r.longeur)
    # print(r.__dict__)

    print(r)
    print(int(r))
    r = Rectangle(3,2)
    r1 = Rectangle(3,2)

    if r==r1:
        print("ok")
    else:
        print("ko")
    print(r.__hash__())
if __name__ == '__main__':
    main()