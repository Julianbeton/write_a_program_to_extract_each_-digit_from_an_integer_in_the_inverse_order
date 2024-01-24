# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def reverse_digits(integer):
   
    given_integer = str(integer)
    
    for digit in given_integer[::-1]:
        print(digit, end=" ")

given_integer = 7536
print("\033[1;32;40mGiven integer:", given_integer)
print("Output integer in reverse order:", end=" ")

reverse_digits(given_integer)
