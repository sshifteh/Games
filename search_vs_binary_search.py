


def search(alist, number):

        if number in alist:
                return True
        else:
                return False





def binary_search(alist, number):

        start_index = 1
        stop_index = len(alist)

        var = False

        while var == False:
                middle_index = int((stop_index - start_index) / 2.)
                print 'middle_index', middle_index
                print 'alist[middle_index]', alist[middle_index]
                print 'number', number

                if number == alist[middle_index]:
                            print 'end'
                            var = True

                elif number > alist[middle_index]:
                            print 'bigger'

                            if len(alist) == 1 and alist[0] != number:
                                        print 'number not in list'



                            start_index = middle_index+1
                            alist = alist[start_index:]
                            print 'alist[start_index:]', alist
                            var = False

                            if len(alist) == 1 and alist[0] != number:
                                        print 'number not in list'
                                        break




                elif number < alist[middle_index]:
                            print 'smaller'

                            stop_index = middle_index


                            if  stop_index == 0 and alist[0] != number:
                                        print 'number not in list'
                                        break




                            print 'stop_index', stop_index
                            alist = alist[:stop_index]
                            print 'alist[start_index:]', alist
                            var = False






        return var


alist = [1,2,3,4,5,6]
number = -3
print binary_search(alist, number)
