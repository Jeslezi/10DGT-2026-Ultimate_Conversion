#Ultimate Conversion Calculator
#Version 1
#Author: Jesse Lin
#Date: 3 June 2026

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
    error = "Please enter a valid distance unit\n"
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

def mass_checker(question):
    
    #Error statement
    error = "Please enter a valid mass unit\n"
    while True:
        
        try:
            #Ask the user for the width
            response = str(input(question))
            #Checks all the different length conversions
            #Checks if the the conversion is valid
            if response == "g":
                return response
            elif response == "kg":
                return response
            elif response == "t":
                return response
            else:
                #If it isn't print the error code   
                print(error)
        except ValueError:
            print(error)

def time_checker(question):
    
    #Error statement
    error = "Please enter a valid time unit\n"
    while True:
        
        try:
            #Ask the user for the width
            response = str(input(question))
            #Checks all the different length conversions
            
            #Checks if the the conversion is valid
            if response == "seconds":
                return response
            elif response == "minutes":
                return response
            elif response == "hours":
                return response
            elif response == "days":
                return response
            else:
                #If it isn't print the error code   
                print(error)
        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
#Main routine
#Ask for what type of conversion
    print("Welcome to the Ultimate Conversion Calculator")
    instructions = input("Press enter for instructions or any other key to skip:")
    if instructions == "":
        print("Types of conversion are")
        print("distance")
        print("mass")
        print("time")
    type_of_conversion = type_checker("Type of conversion:") 

    if type_of_conversion == "distance":
        #Ask if they want instruction
        instructions = input("\nPress enter for instructions or any other key to skip:")
        if instructions == "":
            print("units for converting distance are")
            print("mm")
            print("cm")
            print("m")
            print("km") 
        first_conversion = distance_checker("\nFirst Conversion:")
        second_conversion = distance_checker("Second Conversion:")
        conversion = (f"{first_conversion} to {second_conversion}")
        
    if type_of_conversion == "mass":
        instructions = input("\nPress enter for instructions or any other key to skip:")
        if instructions == "":
            print("units for converting mass are")
            print("kg")
            print("g")
            print("t")
        first_conversion = mass_checker("\nFirst Conversion:")
        second_conversion = mass_checker("Second Conversion:")
        conversion = (f"{first_conversion} to {second_conversion}")

    if type_of_conversion == "time":
        instructions = input("\nPress enter for instructions or any other key to skip:")
        if instructions == "":
            print("units for converting time are")
            print("seconds")
            print("minutes")
            print("hours")
            print("days") 
        first_conversion = time_checker("\nFirst Conversion:")
        second_conversion = time_checker("Second Conversion:")
        conversion = (f"{first_conversion} to {second_conversion}")

    if conversion == "mm to cm":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 10
        print(f"{unit} mm to cm is equal to {output} cm")

    if conversion == "mm to m":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 1000
        print(f"{unit} mm to m is equal to {output} m")

    if conversion == "mm to km":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 1000000
        print(f"{unit} mm to km is equal to {output} km")

    if conversion == "cm to m":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 100
        print(f"{unit} cm to m is equal to {output} m")

    if conversion == "cm to km":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 100000
        print(f"{unit} cm to km is equal to {output} km")

    if conversion == "cm to mm":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 10
        print(f"{unit} cm to mm is equal to {output} mm")

    if conversion == "m to mm":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 1000
        print(f"{unit} m to mm is equal to {output} mm")

    if conversion == "m to cm":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 100
        print(f"{unit} mm to cm is equal to {output} cm")

    if conversion == "m to km":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 1000
        print(f"{unit} m to km is equal to {output} km")

    if conversion == "km to mm":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 1000000
        print(f"{unit} km to mm is equal to {output} mm")

    if conversion == "km to cm":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 100000
        print(f"{unit} km to cm is equal to {output} cm")

    if conversion == "km to m":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 1000
        print(f"{unit} km to m is equal to {output} m")

    if conversion == "g to kg":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 1000
        print(f"{unit} g to kg is equal to {output} kg")

    if conversion == "g to t":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 1000000
        print(f"{unit} g to t is equal to {output} tonnes")

    if conversion == "kg to g":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 1000
        print(f"{unit} kg to g is equal to {output} g")

    if conversion == "kg to t":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 1000
        print(f"{unit} kg to t is equal to {output} tonnes")
        
    if conversion == "t to kg":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 1000
        print(f"{unit} t to kg is equal to {output} kg")

    if conversion == "t to g":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 1000000
        print(f"{unit} t to g is equal to {output} g")
        
    if conversion == "seconds to minutes":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 60
        print(f"{unit} seconds to minutes is equal to {output} minutes")

    if conversion == "seconds to hours":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 3600
        print(f"{unit} seconds to hours is equal to {output} hours")

    if conversion == "seconds to days":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 86400
        print(f"{unit} seconds to days is equal to {output} days")

    if conversion == "minutes to days":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 1440
        print(f"{unit} minutes to days is equal to {output} days")

    if conversion == "minutes to seconds":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 60
        print(f"{unit} minutes to seconds is equal to {output} seconds")

    if conversion == "minutes to hours":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit / 60
        print(f"{unit} minutes to hours is equal to {output} hours")

    if conversion == "days to seconds":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 86400
        print(f"{unit} days to seconds is equal to {output} seconds")

    if conversion == "days to minutes":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 1440
        print(f"{unit} days to minutes is equal to {output} minutes")

    if conversion == "days to hours":
        unit = num_checker(f"\nHow many {first_conversion}:")
        output = unit * 24
        print(f"{unit} days to hours is equal to {output} hours")

    #Ask user if they want to keep going
    keep_going = input("\nPress enter to keep going or any key to quit. ")
    print()

print("Thank you for using the ultimate conversion calculator")





