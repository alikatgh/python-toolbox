def power(number, pow=1):
    """raise number to the power of pow"""

    new_value = number ** pow
    return new_value

power(19.2, 4.1)
power(4.1)

def add_all(*args):
    """sum all values in *args together"""

    # initialize sum
    sum_all = 0

    # accumulate the sum
    for num in args:
        sum_all += num 
    
    return sum_all

add_all(1)
add_all(1, 3)
add_all(1, 3, 3, 933.3)

def print_all(**kwargs):
    """print out key-value pairs in **kwargs"""

    # print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)

print_all(name='dumbledore', job='headmaster')
