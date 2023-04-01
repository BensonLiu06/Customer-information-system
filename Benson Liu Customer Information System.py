# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor

def printMenu(): #prints menu interface where user is allowed to choose an option
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def enterCustomerInfo(): #Customer inputs their info

    

    firstName = input("Enter your First Name: ") #inputs their first name
    lastName = input("Enter your Last Name: ") #inputs their last name
    city = input("Enter what city you are from: ") #inputs their City
    while True:
        postalCode = input("Enter Postal Code: ") #inputs their postal code
        if len(postalCode) >= 3 and validatePostalCode(postalCode): #verifys whether the input is 3 letters/numbers or more and if it passes the validation check
            break
        elif len(postalCode) < 3: #if the postal code is less than 3 letters/numbers it will print invalid and ask for a valid input
            print("invalid Postal Code, please try again")
    
    while True:
        creditCard=input("Credit Card number: ") #inputs Credit Card
        if len(creditCard) >= 9 and validateCreditCard(creditCard): #verifys if the input is more than or equal to 9 digits and checks if it passes the luhn algorithm credit card verification.
            break
        elif len(creditCard) < 9: #if credit card has less than 9 digits, it will print invalid and ask for another input
            print(" Invalid Credit Card Number, please try again")
    
    # appends to a temporary file, if it exists, it will append, if it doesn't it will create a new one
    f = open("CustomerData.csv", "a")

    # reads the file, and gives an ID to every line starting at 1.
    fileRead= open("customerData.csv", "r")
    id=1
    for line in fileRead.readlines():
        id += 1

    # writes the users input and ID in the file.
    f.write(f"{firstName} | {lastName} | {city} | {postalCode} | {creditCard} | {id}\n")
    f.close()

''' 
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validatePostalCode(postalCode): #determines whether the postal code is valid
    try:
        if len(postalCode) < 3: #checks if the postal code is less than 3 digits
            return False
        

        with open("postal_codes.csv", encoding='utf8', errors='ignore') as file:
            for line in file: #CHANGE VARIABLE NAMES

                if line[:3] == postalCode[:3]: #checks the first 3 letters of the postal code and sees if it matches with the file (postal_codes.csv)
                    print("Postal Code Validated")
                    return True #returns true when matches
    
        
        return False #returns false if doesn't match.
    except TypeError:
        print(TypeError)
        print("Enter a valid postal code") #if it does not match what is inside the file
    
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validateCreditCard(creditCard): #determines whether the credit card is valid
    count=1
    reverseNum= (str(creditCard) [::-1]) #reverses the inputted number
    sumofOddNumbers=0 
    for num in str(reverseNum): #loop over all the reversed number
            num=int(num)

            if count % 2 ==1:  #adding each odd index together
                sumofOddNumbers += num 
            count+=1

    if len(str(creditCard)) < 9: #checks if the given input is less than 9
        return False
    
    try:
        reversedNumber = reverseNum 
        
        sum1 = sumofOddNumbers #add all the odd numbers in the input/string
        sum2 = 0
        finalSum = 0
        count = 1

        for num in str(reversedNumber): #loop over all the reversed number
            num=int(num)
            if count % 2 ==0: #adding each even index together, if it's greater than 2 digits, it adds them together
                if num * 2 > 9: 
                    for digit in str(num * 2): #if it's not 2 digits, it will multiply them all together
                        sum2 += int(digit)
                else:
                    sum2+= num * 2 #if it's not 2 digits, it will multiply them all together
            count+=1

        finalSum= sum1+sum2 #adds the sum of the odd numbers and sum of the even numbers together

        if int(str(finalSum) [-1:]) == 0: #if the last digit of the final sum is 0, credit card is validated
            print("Credit Card Validated")
            return True 
        else: #if not, then credit card is invalid.
            print("invalid credit card")
            return False
    except:
        return False
    
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
    '''
def generateCustomerDataFile(): #generates a file with the user's information and their unique ID code    
    output_file = input("enter output file name: ") #user decides what the file is called
    filePath = input("Enter a file path: ") #user decides a path to find the file
    fileName = output_file + ".csv" #names the output file what the user inputted and adds .csv as the file extension
    fileCreate = filePath + fileName #creates the file

    #opens temporary file and adds what was in the temp file into the file that is created on the user's computer.
    with open('CustomerData.csv','r') as firstfile, open(fileCreate,'a') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)


####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables

userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        enterCustomerInfo()
    
    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")