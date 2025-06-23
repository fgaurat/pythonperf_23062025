
def add(*l): # paramètres positionnels en nombre variable *args
    print(l) # tuple
    r = 0
    for i in l:
        r+=i

    return r


# HelloWorld => PascalCase, UpperCamelCase
# helloWorld => camelCase
# hello_world => snake_case
# hello-world => kebab-case, train-case, spin-case

def hello(**kwargs):
    # print("Hello",name,first_name)
    print(kwargs['first_name'])


#def f(a,b,/): # pos only
#def f(*,a,b): # kw only
# =>  f(a,b, /c,d,*,e,f): # 
#       pos, pos_kw ,kw

# def f(a,b,/): # pos only
#     print(a,b)

def f(*,a,b): # kw only
    print(a,b)


def simple_add(a:int,b:int)->int:
    """
    return sum of a and b
    """
    return a+b

# Function
def main():
    # region pos params
    # TDD Test driven development
    # Arrange
    l=[10,20,30,40,50]

    # Act
    # r = add(l)
    r = add(*l) # 10,20,30,40,50<=[10,20,30,40,50]

    # Assert 
    # print(r) # ?150
    # assert r == 152
    # r = 150

    r = add(10,20,30,40,50)
    print(r)

    a,b,*c = 0,1,2,3,4,5
    *a,b,c = 0,1,2,3,4,5
    a,*b,c = 0,1,2,3,4,5
    print(a,b,c)
    # a,b=0,1

    # a,b,c= 0,1
    l=[10,20,30,40,50]
    # a,b,*c = [*l]

    # a,b,c,d,e = 0,1,2


    # print(l) # print([10,20,30,40,50])
    # print(*l) # print(10,20,30,40,50)
    print(*l,sep=';')
    # endregion
    
    hello(first_name="Fred",name="GAURAT",job="dev")

    d = {
        "first_name":"Fred",
        "name":"GAURAT",
        "job":"dev"
    }
    hello(**d)
    r = simple_add("toto","tutu")
    print(r)

    # f(1,2)

    # f(a=1,b=2)
    s = """
ligne 01
ligne 02
ligne 03
"""
    print(s)
if __name__ == '__main__':
    main()