import argparse

def factorial(p):
        if p == 0:
            return 1
        else:
            p *= factorial(p-1)
            return p

def verifying_test():
        if factorial(3) == 6:
                print "factorial works"
        else:
                print "factorial does not workS "

def main():
    parser = argparse.ArgumentParser()
    group =  parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", help = "Give explanation", action = "store_true")
    group.add_argument("-q", "--quiet", help = "Give result only ", action = "store_true")

    parser.add_argument("num", help ="The factorial you wish to calculate", type= int)
    args = parser.parse_args()
    result = factorial(args.num)


    if args.verbose:
        print "The factorial of %s is %s" %(args.num, result)
    elif args.quiet:
        print "%s!=%s" %(args.num, result)
    else:
        print "factorial %s!=%s" %(args.num, result)

if __name__ == "__main__":
        #verifying_test()
        main()