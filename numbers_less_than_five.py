
number = int(raw_input('Enter number: '))

alist = [1,2,3,4,5,6,7,8,9,10]

for i in alist:
        if i < 5:
                print i


new_list = [i for i in alist if i < number]
print new_list