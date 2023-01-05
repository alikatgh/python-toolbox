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

# Define shout_echo
def shout_echo(word1, echo, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey', echo=5, intense=True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey', echo=1, intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)