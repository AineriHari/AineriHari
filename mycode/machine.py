#program for available phones using function

def phones():
    available = int(input("enter the total available mobiles : ".lstrip().capitalize()))
    iteration_available = available
    c = 0
    while c <= iteration_available:
        n = int(input("enter the mobiles you want : ".lstrip().capitalize()))
        if n <= available:
            print("you got {} mobiles".format(n).lstrip().capitalize())
            available -= n
            print("available mobliles are {}".format(available).lstrip().capitalize())
            c += 1

        else:
            if n >= available:
                print("you got {} mobiles".format(available).lstrip().capitalize())
                print("out of stock".lstrip().capitalize())
                break
            else:
                print("out of stock".lstrip().capitalize())
                break


if __name__ == '__main__':
    mobiles = phones()