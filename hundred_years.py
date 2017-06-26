
import sys

def get_info():
    try:
        name = sys.argv[1]
        age = sys.argv[2]
    except IndexError:
        name = raw_input("Enter name: ")
        age = raw_input("Enter age: ")
    return name, age

def hundred_years(name, age):
     this_years = 2017
     hundred = this_years + (100 - age)
     print " Dear %s in the year %g you will be a 100 years ! " %(name, hundred)


def main():
    name, age = get_info()
    hundred_years(name, float(age))

if __name__ =="__main__":
        main()

        """

        Example output and how to run the program in the terminal:

        Pedrams-Mac-mini:shareactor_ shiftehsherafat$ python hundred_years.py
        Enter name: Shifteh
        Enter age: 27
        Dear Shifteh  in the year 2090 you will be a 100 years !

        """

