from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(3)
    print(c.surface)
    print(c.longueur)
    print(c.largeur)

    ce = Cercle(3)
    print(f"{ce.rayon=}")
    print(f"{ce.surface=}")

    print(type(c))
    print(type(Carre))


    print(type(2))
    print(type(int))

if __name__ == '__main__':
    main()