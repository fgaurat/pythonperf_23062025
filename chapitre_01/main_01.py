import lib
import the_packages.module1
import the_packages.other_packages.module3 as m3

from the_packages.other_packages.module3 import truc3

from the_packages import module1
from the_packages.module1 import truc1



def truc3():
    print("un autre truc3")

def main():
    lib.hello("Fred")
    the_packages.module1.truc1()
    m3.truc3()
    truc3()
    module1.truc1()

if __name__ == '__main__':
    main()