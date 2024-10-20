def sales_prices(item_and_price):
    # Initialize variables "item" and "price" as strings
    item = ""
    price = ""
    # Create a variable "item_or_price" to hold the result of the split. 
    item_or_price = item_and_price.split()

    # For each element "x" in the split variable "item_or_price" 
    for x in item_or_price:

        # Check if the element is a letter
        if x.isalpha():

            # If true, assign the element to the "item" string variable and add a space 
            # for any item names containing multiple words, like "Winter fleece jacket".
            item += x + " "

        # Else, if x is a number (if x.isalpha() is false): 
        else:
            # Assign the element to the "price" string variable. 
            price = x

    # Strip the extra space to the right of the last "item" word
    item = item.strip()

    # Return the item name and price formatted in a sentence 
    return "{} are on sale for ${}".format(item,price)


# Call to the function 
print(sales_prices("Winter fleece jackets 49.99"))
# Should print "Winter fleece jackets are on sale for $49.99"


# This function accepts a string variable "data_field".  
def count_words(data_field):

    # Splits the string into individual words. 
    split_data = data_field.split()
  
    # Then returns the number of words in the string using the len()
    # function. 
    return len(split_data)
    
    # Note that it is possible to combine the len() function and the 
    # .split() method into the same line of code by inserting the 
    # data_field.split() command into the the len() function parameters.

# Call to the function
print(count_words("Catalog item 3523: Organic raw pumpkin seeds in shell"))
# Output should be 9