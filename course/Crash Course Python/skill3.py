# The function accepts two parameters: a start year and an end year
def list_years(start, end):
# It returns a list comprehension that creates a list of years in a for
# loop using a range from the start year to the end year (inclusive of 
# the upper range year, using end+1).
  return [year for year in range(start, end+1)]

# Call the list_years() function with two parameters.
print(list_years(1972, 1975)) 
# Should print [1972, 1973, 1974, 1975]

# The function accepts two variable integers through the parameters and
# returns all odd numbers between x and y-1.
def odd_numbers(x, y):


# This list comprehension uses a for loop to iterate through values 
# of n in a range from x to y, with the value of y excluded (meaning
# keep the default range() function behavior to exclude the
# end-of-range value from the range). Since an incremental value is not 
# specified, the range function uses the default increment of +1.
# The if condition checks n to test if the number is odd using the
# modulo operator. This condition is written to check if n is divided 
# by 2, that the remainder is not 0. 
    return [n for n in range(x, y) if n % 2 != 0]


# Call the odd_numbers() function with two parameters.
print(odd_numbers(5, 15)) 
# Should print [5, 7, 9, 11, 13]