
alist = [1,2,3,4,98,76,24]



def less_than_10(alist):
    for i in alist:
            if i <10:
                yield i

result = less_than_10(alist)
print result # generator object
print result.next()
for i in result:
        print i