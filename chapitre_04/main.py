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

if __name__ == '__main__':
    main()