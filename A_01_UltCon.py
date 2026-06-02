#Create conversion checker
# Author Jesse Lin
#02 June 2026
# Version 1

'''#Code to check whether the conversion is valid(V1)
def conversion_checker(question):
    
    #Error statement
    error = "Please enter a valid conversion\n"
    while True:
        
        try:
            #Ask the user for the width
            response = str(input(question))
            #Checks all the different length conversions
            #Checks if the the conversion is valid
            if response == "mm to cm":
                return response
            elif response == "cm to m":
                return response
            elif response == "m to km":
                return response
            elif response == "cm to km":
                return response
            elif response == "mm to km":
                return response
            elif response == "mm to m":
                return response
            else:
                #If it isn't print the error code   
                print(error)
        except ValueError:
            print(error)
            
            
conversion = conversion_checker("\nWhat method of conversion ")'''

#Code to check whether the conversion is valid(V2)
'''def conversion_checker(question):
    
    #Error statement
    error = "Please enter a valid conversion\n"
    while True:
        
        try:
            #Ask the user for the width
            response = str(input(question))
            #Checks all the different length conversions
            #Checks if the the conversion is valid
            if response == (f"first_conversion to second_conversion"):
                return response
            else:
                #If it isn't print the error code   
                print(error)
        except ValueError:
            print(error)'''

def type_checker(question):
    
    #Error statement
    error = "Please enter a valid type of conversion\n"
    while True:
        
        try:
            #Ask the user for the width
            response = str(input(question))
            #Checks all the different length conversions
            #Checks if the the conversion is valid
            if response == "distance":
                return response
            elif response == "time":
                return response
            elif response == "mass":
                return response
            else:
                #If it isn't print the error code   
                print(error)
        except ValueError:
            print(error)

def distance_checker(question):
    
    #Error statement
    error = "Please enter a valid type of conversion\n"
    while True:
        
        try:
            #Ask the user for the width
            response = str(input(question))
            #Checks all the different length conversions
            #Checks if the the conversion is valid
            if response == "mm":
                return response
            elif response == "m":
                return response
            elif response == "cm":
                return response
            elif response == "km":
                return response
            else:
                #If it isn't print the error code   
                print(error)
        except ValueError:
            print(error)

#Main routine
type_of_conversion = type_checker("Type of conversion: ") 

if type_of_conversion == "distance":
    first_conversion = distance_checker("\nFirst unit  ")
    second_conversion = distance_checker("\nSecond unit  ")
    conversion = (f"{first_conversion} to {second_conversion}")

if conversion == "cm to m":
    print("hello")





