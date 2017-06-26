import re


def splitFirst(expression):
        """
        splitFirst() searches through a string that is a mathematical expression and finds the first number, symbol and remaining of expression.
        Example:
            >>> splitFirst("2+3*4")
            >>> '2','+','3*4'


        :param expression: mathematical expression provided by user
        :return: the first number in the expression, the symbol after the number, and the rest of the expression.
        or if there is no more symbols or expression remaning, the final number, None, and an empty string.
        """


        pattern = re.compile(r'\*|-|\+|/')   # regex pattern for the operators +-/*
        m = re.search(pattern, expression)   # searching for the pattern in the expression

        if m != None:                         # if something is found

            symbol = m.group(0)               # symbol is the first group
            #print "symbol: ", symbol
            symbol_index = expression.find(symbol) # and we want the index for the symbol in expression. in this case it is indeks 2
            #print "symbol_index:", symbol_index

            first = expression[symbol_index-1]   # first is indeks 1
            symbol_ = expression[symbol_index]   # symbol is indeks 2
            rest = expression[symbol_index+1:]   # and rest is the rest of the indexes
            print "INSIDE SPLITFIRST first:", first,"symbol_: ", symbol_, "rest: ", rest
            return first, symbol_, rest

        else:
            print " IN  SPLITFIRST expression", expression, None, ''
            return expression, None, ''





def substring_catcher(expression):
            """
            substring_catcher manipulates the input expression to extract the argument inside parenthesis.
            Exmaple:
                    expression = (2+4)*3
                    returns 2+4

            :param expression: mathematical expression provided by user.
            :return: the inside of the paranthesis if there were parenthesis in the input expression.
            """

            expression_ = expression.replace(' ', '')  # remove whitespace
            par_pattern = re.compile(r"\((.+)\)")      # regex pattern to search for anything inside parenthesis
            m = re.search(par_pattern, expression_)    # search for it within expression
            substring = m.group(0)                     # anythings inside parenthesis including parenthesis are group(0)
            return substring[1:-1]                     # Thus we keep only the inside argument







def simple_calculator(expression):
    """
    simple_calculator() takes a mathematiacal expression as string as input and return the result.
    :param expression: string mathematical expression with binary operations +-/*
    :return: the result


    An example session is as follows:

    This is a simple calculator that will solve simple mathematical expressions.
    An example expression is 1*2+3
    With the output result: 5

    Enter expression: 3/3+1
    result:  2.0

    """


    expression_ = expression.replace(' ', '')

    print "CALC"
    first, symbol, rest = splitFirst(expression_)
    print "IN CALC first", first, "symbol", symbol, "rest", rest
    a = 0
    b = float(first)
    print "b", b
    print  "a",a

    while symbol is not None:
        first, nextsymbol, rest = splitFirst(rest)
        print "IN CALC first", first, "nextsymbol", nextsymbol, "rest", rest
        if symbol == '*':
            b *= float(first)
        elif symbol == "/":
            b /= float(first)
        elif symbol == '+' or '-':
            a += b
            if symbol == '+':
                b = float(first)
            else:
                b =- float(first)
        symbol = nextsymbol
    a += b
    print a
    return a


if __name__ == "__main__":

    # Simple API:
    #print ''
    #print "This is a simple calculator that will solve simple mathematical expressions "
    #print "An example expression is 1*2+3 "
    #print "With the output result: 5  "
    #print ''
    #try:
        #expression = raw_input("Enter expression: ")
        #print "result: ", simple_calculator(expression)

    #except ValueError:
    #        print "Failed to enter expression."

    expression = "1*2+3"
    simple_calculator(expression)