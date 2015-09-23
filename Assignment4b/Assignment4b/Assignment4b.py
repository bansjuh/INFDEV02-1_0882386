while True:
    C = int(input("Enter a temperature in Celsius: "))    
    if ( C > -273.15):
        K = C  + 273.15
        print ("Temperature:", C, "Kelvin = ", K, " K")
        break
    else:
        print(" This is not a valid temprature ")