import traceback

class DivBy12Exception(Exception):

    def __init__(self) -> None:
        super().__init__("Division par 12 !")

def div(a,b):

    if b ==12:
        raise DivBy12Exception()
    return a/b

def call_div(a,b):
    r = 0
    try:
        print('OPEN')
        r = div(a,b)
    # except Exception as e:
    #     print(e)
    #     raise e
    finally:
        print('CLOSE')
    
    return r

def main():
    try:
        a=2
        # b=int(input('b:'))
        b=12
        # c= a / b
        c = call_div(a,b)
        print(c)

    # except ZeroDivisionError as e:
    #     traceback.print_exc()
    # except ValueError as e:
    #     print("erreur",e)
    #     traceback.print_exc()
    except Exception as e:
        print("erreur",e.__class__.__name__)
        traceback.print_exc()
    else:
        print("pas d'erreur")
    finally:
        print("finally")


    print("... la suite du code")

if __name__ == '__main__':
    main()