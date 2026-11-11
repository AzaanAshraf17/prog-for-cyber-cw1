#Import the nesscary modules for the security functions
import random
import string

#A Function that validates the password that is enterned by the user
def validate_password(password):

    #passwords has to be atleast 8 Characters long to be secure
    if len(password) < 8:
        return False

    has_letter = False
    has_integer = False
    has_symbol = False

    #Check each charater in the passwrd
    for char in password:

        if char.isalpha():
            has_letter = True

        elif char.isdigit():
            has_integer = True

        else:
            has_symbol = True

    #Check the password to see if it contains a letter , number or special characters
    if has_letter and has_integer and has_symbol:
        return True

    return False


# A function to validate an IP Address that is entered by the user
def validate_ip_address(ip_address):

    #Remove the spaces before and after from the IP
    ip_address = ip_address.strip()

    #Check and ensure the IP contains 3 dots and 4 octets
    if ip_address.count(".") != 3:
        return False

    #Split the Ip address into its 4 ocetts
    parts = ip_address.split(".")

    # Check to see if the IP has exactly 4 ocetets
    if len(parts) != 4:
        return False

    #Check each ocetet to ensure it only contains numbers and the numbers are between 0 and 255
    for part in parts:

        if not part.isdigit():
            return False

        number = int(part)

        if number < 0 or number > 255:
            return False

    return True


# A funtion to generate a strong password for the user to use
def generate_strong_password():

    #Password length to be between 10 to 16 characters long
    length = random.randint(10,16)

    uppercase_letters = random.choice(string.ascii_uppercase)
    Lowercase_letters = random.choice(string.ascii_lowercase)
    integer = random.choice(string.digits)

    characters_list = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""

    # Generate the random password selected from the characters list !@#$%^&*"
    for i in range(length):
        password += random.choice(characters_list)

    return password
