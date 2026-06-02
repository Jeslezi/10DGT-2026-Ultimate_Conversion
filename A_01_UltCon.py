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
    error = "Please enter a valid length unit\n"
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

def num_checker(question):
    
    #Error statement
    error = "Please enter a valid number or a number that is more than zero\n"
    while True:
        
        try:
            #Ask the user for the width
            response = float(input(question))
            
            #Checks if the width is more than zero
            if response > 0:
                return response
            else:
                #If it isn't print the error code   
                print(error)
        except ValueError:
            print(error)
#Main routine








