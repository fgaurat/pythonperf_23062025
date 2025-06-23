

toto = 12

def hello(name):
    # toto
    # global toto
    print("Hello",name)
    
    print("hello toto",toto)
    if False:
        toto = 13


if __name__ == "__main__":
    print("__name__",__name__)
    print("avant",toto)
    hello('Fred')
    print("après",toto)