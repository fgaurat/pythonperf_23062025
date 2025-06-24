from Test import Test
from RectangleSingleton import RectangleSingleton

def main():
    # t = Test()
    # print(t.toto)
    # t()
    r = RectangleSingleton()
    r1 = RectangleSingleton()
    print(hex(id(r)))
    print(hex(id(r1)))





if __name__ == '__main__':
    main()