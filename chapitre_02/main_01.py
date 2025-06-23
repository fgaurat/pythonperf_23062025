
def make_incrementor(i):
    
    
    def the_function(j):
        return i+j

    return the_function

def main():
    
    do_inc = make_incrementor(10)
    
    r = do_inc(3) 
    print(r) # 13

    r = do_inc(5) 
    print(r) # 15

if __name__ == '__main__':
    main()