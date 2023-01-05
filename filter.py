fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

"""
In the `filter()` call, pass a lambda function and the list of strings, `fellowship`. The lambda function should check if the number of characters in a string `member` is greater than 6; use the `len()` function to do this. Assign the resulting filter object to `result`.

Convert `result` to a list and print out the list.

"""

"""
HINTS: 

- The first argument to `filter()` should be the lambda function and the second argument is the list `fellowship`. Pass a string to `len()` to get the number of characters in the string.

 - To convert the filter object to a list, use the `list()` function.

"""

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 5, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)