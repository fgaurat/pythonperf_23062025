from functools import wraps

# def call_say_hello(name:str)->str:
#     print("in",name)
#     s = say_hello(name)
#     print("out",s)
#     return s


def do_log(log_file):
    def decorator(func ):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(f"write log to {log_file} in ",args,kwargs)
            r = func(*args,**kwargs)
            print(f"write log to {log_file} out",r)
            return r
        
        return wrapper

    return decorator


def do_secu(func):

    def wrapper(*args,**kwargs):
        print("the secu",args,kwargs)
        r = func(*args,**kwargs)
        return r
    
    return wrapper

# do_log | do_secu | do_log say_hello
# @do_log('lefichier.log')
# @do_secu

@do_log('lefichier.log')
def say_hello(name:str)->str:
    """
    Dire Bonjour à name
    """
    s = f"Bonjour {name}"
    return s

def main():
    # r = call_say_hello('Fred')
    r = say_hello('Fred')
    print(r)

    print(say_hello.__name__)
    print(say_hello.__doc__)

if __name__ == '__main__':
    main()





