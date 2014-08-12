# Script to illustrate variables
#

# Variable definition
mystring = "eyo"
myfloat = float(100)
myint = 25

# Testing block
if mystring == "eyo":
    print "String %s" % mystring

if isinstance(myfloat, float) and myfloat == 100.0:
    print "Float %d" % myfloat

if isinstance(myint, int) and myint == 25:
    print "Int %d" % myint
