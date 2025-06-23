
default_value="toto"

def f(a=default_value):
    print(a)



default_value = "une autre valeur"

def main():
    # f("truc")
    f()

if __name__ == '__main__':
    main()