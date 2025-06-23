# For/Else
def main():
    l=[10,20,30,40,50]

    to_find = 300
    # found = False

    for i in l:
        print(i)
        if i == to_find:
            print("found")
            break
            # found = True
    else:
        print('ko')

    # if found:
    #     print("ok")
    # else:
    #     print("ko")

if __name__ == '__main__':
    main()