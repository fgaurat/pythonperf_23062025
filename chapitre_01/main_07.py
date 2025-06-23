def old_mult2(the_list):
    r = []

    for i in the_list:
        r.append(i*2)

    return r

def mult2(i):
    return i*2

def main():
    l=[10,20,30,40,50]

    # l2 = list(map(mult2,l))

    
    l2 = list(map(lambda i:i*2,l))   

    print(l2) # [20,40,60,80,100]


    
    

    l=[10,20,30,40,50]
    l2 = []
    for i in l:
        l2.append(i*2)
    print(l2)

    l2 = list(map(lambda i:i*2,l))

    
    l2 = [i*2 for i in l if i%2 == 0] # List Comprehension

if __name__ == '__main__':
    main()