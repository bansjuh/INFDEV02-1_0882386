#-----------------------------------------------------------------------------------------------------
#
# Created by:           Julian Mansveld
# Time Created:         23/10/2015
# Class:                INV1B
# Student Number:       0882386
#
#------------------------------------------------------------------------------------------------------

while True:
    C = input("Enter a temperature in Celsius: ")
    # if the input is bigger then -273.15 then execute the formula to print temps in kelvin.   
    if ( C > -273.15):
        K = C  + 273.15
        print "Temperature:", C, "Kelvin = ", K, " K"
        #break exits the loop befor the given object is finished. 
        break
    else:
        #if the value that is entered is not a temprature it will print this message
        print "This is not a valid temprature"