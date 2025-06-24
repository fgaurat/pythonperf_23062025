class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B,C):

    def show(self):
        super().show()
        super(B,self).show()
        super(C,self).show()
        print("D")

def main():
    
    # print(D.mro())
    # d,b,c,a,*r = D.mro()

    # o = a()
    # o.show()
    d = D()
    d.show()

if __name__ == '__main__':
    main()