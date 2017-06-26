
def largest(number1, number2,number3):

        alist = [number1, number2, number3]

        largest = alist[0]
        for i in alist:
                if i > largest:
                        largest = i

        return largest


print largest(1,2,3)
