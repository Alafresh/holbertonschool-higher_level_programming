#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if count < x:
                print("{:d}".format(i), end="")
            elif count is x:
                break
            count += 1
        except:
            pass
    print()
    return count
