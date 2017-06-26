
def search(olist, number):
    inlist = False
    for  item in olist:
            if number == item:
                    inlist = True

    return inlist





number = 6

ordered_list = [11,12,13,14,15,16,17,18,19]

middle_index = int(len(ordered_list)/2)
middle_element = ordered_list[middle_index]

if number == middle_element:
        print "True"

elif number < middle_element:
        print "less"
elif number > middle_element:
        print "larger"


"""

inlist = False
#while inlist is not True:


if number == ordered_list[middle]:
            print "round"
            print ordered_list[middle]
            inlist = True

elif number > ordered_list[middle]:
            ordered_list  = ordered_list[middle+1:]
            print "larger"
            print ordered_list[middle+1:]

elif number < ordered_list[middle]:
            ordered_list = ordered_list[:middle]
            print "smaller"
            print ordered_list[:middle]
else:
        pass

"""


