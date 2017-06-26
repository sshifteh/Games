import argparse

def fib(n):
        a = 0
        b = 1
        for i in range(n):
                a = b
                b = a+b
        return a


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action = "store_true")
    group.add_argument("-q", "--quiet", action = "store_true")

    parser.add_argument("num", help = "The Fibonacci number you wish to calculate", type= int)
    parser.add_argument("-o", "--outputToFile", help = "Output the result to a file", action = "store_true")

    args = parser.parse_args()
    result = fib(args.num)

    if args.verbose:
            print "The %s fibonacci number is %s" %(args.num,result)

    elif args.quiet:
            print result
    else:
           print "fib(%s)=%s"  %(args.num, result)

    if args.outputToFile:
            f = open("fibonacci.txt", "a") # appending
            f.write(str(result) + "\n")
if __name__ == "__main__":
        main()
