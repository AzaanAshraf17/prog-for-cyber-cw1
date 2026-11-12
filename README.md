prog-for-cyber-cw1
-

Ip Validator Program
-

student details Name: Azaan Ashraf 
-
Banner ID: B01860586 
-
the campus I go to is UWS Lanarkshire Campus 
-

Description of the Program and how the program works
-

This Program is an IP Address Validator it checks to see Whether the IP entered by the user is a valid IP address. The function that is used in the program is validate_ip() this function basically verifies that the IP address follows the correct layout and format of what an IP Should be.

The program will check that the Ip address contains 4 numbers that are separated by dots and that each number is within the valid range of 0 to 255.

The program works by using the function validate_ip () this contains validation checks. So when the user enters an Ip address this function will do the following. 

1.Remove any spaces before and after the IP address.

2.Checks that the IP contains Dots as IP must contain them. 

3.Checks that the IP address contains 3 dots.

4. It will split the IP address into 4 separate sections that are called octets.
   
5. Program checks that there are 4 octets.
   
6. Program will then verify each octet contain only a integer value.
   
7. Program checks that each octet is between the value 0 - 255.

if the all the checks made by the function are true the program will display that the IP address is valid to the user.

if the any checks made by the function are false the program will then display The IP address is invalid please enter again to the user.

the file used is IP validator.py
-

how to run this file in VScode
-
Step 1 - download the file

Step 2 - Open the File on your Computer

Step 3 - Open the terminal of VScode

Step 4 - Navigate to where you have saved the program in your files

Step 5 - Run the file


