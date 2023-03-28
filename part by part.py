def enterCustomerInfo():
    global postal_code
    global credit_card

    first_name=input("Enter First Name: ")
    last_name=input("Enter Last Name: ")
    city=input("Enter City: ")
    postal_code=input("Postal Code: ")
    credit_card=int(input(" Credit Card Number: "))

def validatePostalCode():
    all_postal_codes = 'postal_codes'
    with open(all_postal_codes) as checkPostalCodes:
        postalCodeRead = checkPostalCodes.read()
    if postal_code in postalCodeRead and len(postal_code) >=3:
        print("postal Code validated")
    elif postal_code not in postalCodeRead and len(postal_code) <=3:
        print("invalid postal_Code")

enterCustomerInfo()
validatePostalCode()