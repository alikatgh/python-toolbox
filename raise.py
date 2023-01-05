def raise_both(val1, val2):
    nval1 = val1 ** val2
    nval2 = val2 ** val1

    new_tuple = (nval1, nval2)
    
    return new_tuple

result = raise_both(2,2)
print(result)

# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, num2, num3)