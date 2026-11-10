# Def validate_IP Function - to check IP address is valid, IP address validator program
def validate_ip(ip):

    # will Remove any spaces before or after the IP address is entered
    ip = ip.strip()

    #  will Check to see if the IP contains dots (IP address should always contain dots)
    if "." not in ip:
        return False

    #  will Check to see if there are 3 dots in the IP
    if ip.count(".") != 3:
        return False

    #  will Split the IP address into parts called octets  
    parts = ip.split(".")

    #  will Check that there are 4 octets in IP
    if len(parts) != 4:
        return False

    # Check each part of the IP address
    for part in parts:

        # will Check that the part only contains numbers for the IP  
        if not part.isdigit():
            return False

        # Convert the part to an integer
        number = int(part)

        # will Check that the number is between 0 - 255
        if number < 0 or number > 255:
            return False

    # If all checks are valid then the IP is valid
    return True


# Ask the user for their IP
ip_address = input("Enter an IP address: ")

# Check if the IP is valid and prints the results to the user
if validate_ip(ip_address):
    print("The IP address is valid")
else:
    print("The IP address invalid please enter a valid IP address") 
