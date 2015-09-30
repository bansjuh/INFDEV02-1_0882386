#-----------------------------------------------------------------------------------------------------
#
# Created by:           Julian Mansveld
# Time Created:         23/10/2015
# Class:                INV1B
# Student Number:       0882386
#
#------------------------------------------------------------------------------------------------------

Fahrenheit = input("enter a temprature in fahrenheit: ")
#(?F - 32) x 5/9 = ?C
Celsius = (Fahrenheit - 32) * 5.0/9.0
# first gives back the input from first line to confert it to celsius rounded down to 2 decimals
print "Temperature:", Fahrenheit, "Fahrenheit = ", (round(Celsius,2)), " C"