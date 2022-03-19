#defining program to find the given number is prime or not using function

#def prime(n):
#    if n == 1 or n == 2:
#        print("{} is a prime".format(n).capitalize())
#    else:
#        for i in range(2, n):
#           if n % i == 0:
#                print("{} is not a prime".format(n).capitalize())
#                break
#            else:
#                print("{} is prime".format(n).capitalize())

#n = int(input("enter the number : ").lstrip().capitalize())
#if __name__ == '__main__':
#    primeornot = prime(n=n)
#-------------------------------------------------------------------------------

#def prime(n):
#    if n == 1 or n == 2:
#        return True
#    else:
#        for i in range(2, n):
#           if n % i == 0:
#                return False
#           else:
#                return True

#n = int(input("enter the number : ").lstrip().capitalize())
#if __name__ == '__main__':
#   primeornot = prime(n=n)

#   if primeornot == True:
#       print("{} is a prime".format(n).lstrip().capitalize())

#   else:
#       print("{} is a not prime".format(n).lstrip().capitalize())

#--------------------------------------------------------------------------------

class prime:

    def __init__(self, n):
        self.n = n

    def check(self):
        if n == 1 or n == 2:
            return True
        else:

            for i in range(2, self.n):
                if self.n % i == 0:
                    return False

                else:
                    return True

n = int(input("enter the number : ").lstrip().capitalize())
if __name__ == '__main__':
    primeornot = prime(n=n)

    if primeornot.check() == True:
        print("{} is a prime".format(n).lstrip().capitalize())

    else:
        print("{} is a not prime".format(n).lstrip().capitalize())