#Define/write a function to convert temperature from Celsius to Fahrenheit scale.
#Write some print statements as the main code that will call/test this definition.

def celtofer(celcius):
    farenheight = (celcius * 9) / 5 + 32
    return farenheight

yourinput = float(input("Enter celcius:"))
print("The fahrenheit value of this is: {:0.1f}".format(celtofer(yourinput)))
