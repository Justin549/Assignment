def check(password):
    rules = {#use dictionary storage requirement and result
        "At least 8 characters long": len(password) >= 8,
        "Contains at least one uppercase letter": any(char.isupper() for char in password),
        "Contains at least one lowercase letter": any(char.islower() for char in password),
        "Contains at least one number": any(char.isdigit() for char in password),
    }
    print("\nPassword strength check results:")

    passed = True#record the check result
        
    for rule, result in rules.items():#distribute two items into two variables
        if result:#check the result and print the corresponding output
                print(f"✅ Passed: {rule}")#use icon for better vision 
        else:
                print(f"❌ Failed: {rule}")#once fail in one regulation, change the result status to False
                passed = False

    return passed
                

# Main program

print("Requirement: \nAt least 8 characters long\nContains at least one uppercase letter\nContains at least one lowercase letter\nContains at least one number\n""Enter your password:")
#requirement for the first time

while True:#keep keying until the password is strong enough
    password = input()
    if check(password):#check the result and present
            print("Your password is strong!")
            break
    else:
            print("Your password is not strong. Please try again.\nEnter your password:")