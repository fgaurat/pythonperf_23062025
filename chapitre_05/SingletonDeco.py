from functools import wraps


def singleton(cls):

    instance = None

    @wraps(cls)
    def wrapper(*args,**kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args,**kwargs)
        else:
            instance.__init__(*args,**kwargs)
        
        return instance
    
    return wrapper