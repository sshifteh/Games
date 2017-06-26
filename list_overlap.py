import random

arandom = random.sample(range(20), 5)
brandom = random.sample(xrange(50), 7)



def list_overlap(alist,blist):
    aset = set(alist)
    bset = set(blist)

    return [i for i in aset if i in bset]

print 'arandom',arandom
print 'brandom',brandom

print list_overlap(arandom, brandom)