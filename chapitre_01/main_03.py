import copy
def main():
    l=[10,20,30,40,50]
    print(len(l))
    
    print(l[len(l)-1])
    print(l[-1])
    p = l[1:4] # [1:4[
    print(p)
    p = l[2:]
    print(p)
    p = l[:2]
    print(p)
    p = l[:]
    print(p)
    
    # l1 = l
    l1 = l[:]  # Shallow copy 
    l1 = l.copy()  # Shallow copy 
    l1 = copy.copy(l)  # Shallow copy 
    l[0] = 1000
    print(l)
    print(l1)
    
    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]

    l1 = copy.deepcopy(l)
    l[1][1] = 1000
    print(l)
    print(l1)
if __name__ == '__main__':
    main()