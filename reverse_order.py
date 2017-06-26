

string = "my name is shifteh"
string_list = string.split()
reversed = []
for i in range(len(string_list)):
         reversed.append(string_list[-1-i])

#print reversed


print ' '.join(string.split()[::-1])



def reverse_v1(x):
    y = x.split()
    result = []
    #print y
    for word in y:
      #  print word
        result.insert(0, word)
    #print result
    return " ".join(result)

reverse_v1(string)


# method 4
def reverse_v4(x):
    y = x.split()
    y.reverse()
    return " ".join(y)

#test metode 4:
x = "hei paa deg"
y = x.split()
#print y.reverse()
#print " ".join(y)
