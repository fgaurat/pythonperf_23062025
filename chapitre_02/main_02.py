


# def call_say_hello(name:str)->str:
#     print("in",name)
#     s = say_hello(name)
#     print("out",s)
#     return s


def do_log(func):

    def wrapper(*args,**kwargs):
        print("in",args,kwargs)
        r = func(*args,**kwargs)
        print("out",r)
        return r
    
    return wrapper

def do_secu(func):

    def wrapper(*args,**kwargs):
        print("the secu",args,kwargs)
        r = func(*args,**kwargs)
        return r
    
    return wrapper


    
@do_log
def say_hello(name:str)->str:
    """
    Dire Bonjour à name
    """
    s = f"Bonjour {name}"
    return s

def main():
    r = say_hello('Fred')
    print(r)

if __name__ == '__main__':
    main()