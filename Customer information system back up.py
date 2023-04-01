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

    

    firstName = input("Enter your First Name: ")
    lastName = input("Enter your Last Name: ")
    city = input("Enter what city you are from: ")
    while True:
        postalCode = input("Enter Postal Code: ")
        if len(postalCode) >= 3 and validatePostalCode(postalCode):
            break
        elif len(postalCode) < 3:
            print("invalid Postal Code, please try again")
    
    while True:
        creditCard=input("Credit Card number: ")
        if len(creditCard) >= 9 and validateCreditCard(creditCard):
            break
        elif len(creditCard) < 9:
            print(" Invalid Credit Card Number, please try again")
    
    
    f = open("CustomerData.csv", "a")

    fileRead= open("customerData.csv", "r")
    id=1
    for line in fileRead.readlines():
        id += 1

    f.write(f" {firstName} | {lastName} | {city} | {postalCode} | {creditCard} | {id}\n")
    f.close()

''' 
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validatePostalCode(postalCode): #determines whether the postal code is valid
    try:
        if len(postalCode) < 3:
            return False
        

        with open("postal_codes.csv", encoding='utf8', errors='ignore') as file:
            for line in file: #CHANGE VARIABLE NAMES

                if line[:3] == postalCode[:3]: #checks the first 3 letters of the postal code and sees if it matches with the file
                    print("Postal Code Validated")
                    return True #returns true when match
    
        
        return False #returns false if doesn't match.
    except TypeError:
        print(TypeError)
        print("Enter a valid postal code")
    
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validateCreditCard(creditCard): #determines whether the credit card is valid

    
    count=1
    reverseNum= (str(creditCard) [::-1])
    sumofOddNumbers=0 
    for num in str(reverseNum): #loop over all the reversed number
            num=int(num)

            if count % 2 ==1:
                sumofOddNumbers += num 
            count+=1

    if len(str(creditCard)) < 9:
        return False
    
    try:
        reversedNumber = reverseNum #FIND HOW TO REVERSE THE NUMBER BY GOOGLE
        
        sum1 = sumofOddNumbers #add all the odd numbers in the input/string
        sum2 = 0
        finalSum = 0

        count = 1

        for num in str(reversedNumber): #loop over all the reversed number
            num=int(num)

            if count % 2 ==0:
                if num * 2 > 9:
                    for digit in str(num * 2):
                        sum2 += int(digit)
                else:
                    sum2+= num * 2
            count+=1

        finalSum= sum1+sum2

        if int(str(finalSum) [-1:]) == 0:
            print("Credit Card Validated")
            return True 
        else: 
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
        
    

    output_file = input("enter output file name: ")
    filePath = input("Enter a file path: ")
    fileName = output_file + ".csv"
    fileCreate = filePath + fileName

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