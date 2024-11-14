def is_armstrong_number(number):
    # Convert the number to a string and calculate the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of the cubes of each digit
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    if armstrong_sum == number:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print("It is an Armstrong number \U0001F973")
else:
    print("It is not an Armstrong number \U0001F625")