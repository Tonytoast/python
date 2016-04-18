from sys import argv

#first arg is script name, second is first parameter
script, var1 = argv

print "Script name is: %s and arg given is %s" %(script, var1)

para1="""
This is a paragraph not over 80 characters wide
because apparently they hate that.
\tAnd tabs
"""

print "-----"
print para1
print "----"


number1 = int(raw_input("Enter a number: "))
number1+=1

print "Just added 1 to your number: %d" %(number1)

def add_two(number):
    print "Adding 2 to your number"
    number+=2
    return number

number2 = int(raw_input("Enter second number: "))

print add_two(number2)

