# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.

    ######################
def kilometer_conversion(kilometers):    
    miles = 0.0
    miles=kilometers*0.6214
    return miles

kilometers=float(input("Enter the number of kilometers:"))

miles=kilometer_conversion(kilometers)

print(f"{kilometers} kilometers equals {miles} miles.")
    ######################    


    # Return the variable to the calling function
    #return miles (***NOTE*** I moved this return command into the function; my compiler wouldn't allow me to run the code unless I placed the return in the function.)

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    
    # Display the miles
