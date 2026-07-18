# Check if the password is at least 8 characters long
def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Check if the password contains an uppercase letter
def check_uppercase(password):
    for letter in password:
        if letter.isupper():
            return True

    return False

# Check if the password contains a number
def check_number(password):
    for character in password:
        if character.isdigit():
            return True

    return False

#Check if the password contains special characters
def check_special(password):
    special = "!@#$%^&*"

    for character in password:
        if character in special:
            return True

    return False

# Rate the password strength
def rate_password(score):
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Fair"
    else:
        return "Strong"
    

def main():

    while True:

        password = input("\nEnter a password (or type 'quit' to exit): ")

        if password.lower() == "quit":
            print("Goodbye")
            break

        score = 0

        
        if check_length(password):
            print("YES - Password is at least 8 characters long.")
            score += 1
        else:
            print("NO - Password must be at least 8 characters long.")

       
        if check_uppercase(password):
            print("YES - Contains an uppercase letter.")
            score += 1
        else:
            print("NO - Missing an uppercase letter.")

       
        if check_number(password):
            print("YES - Contains a number.")
            score += 1
        else:
            print("NO - Missing a number.")

        
        if check_special(password):
            print("YES - Contains a special character.")
            score += 1
        else:
            print("NO -Missing a special character.")

       
        print("Password Strength:", rate_password(score))


main()

