
import random

alist = random.sample(xrange(10),5)
blist = random.sample(xrange(15),7)
print alist, blist
overlap = [i for i in set(alist) if i in set(blist)]
print overlap