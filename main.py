def is_narc(n):
    """Check if a number is narc."""
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == n

def print_narcis_numbers(start, end):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1)
        if is_narc(num)
            print(num)

print_narcis_numbers(1000, 5000)

#added colon after function definitions
#correction function call names
#added comma between arguments to function call in line 10 
#changed three * to two * to perform power operation
#Changed the == in the num_str and num_digits to = as we are assigning values
