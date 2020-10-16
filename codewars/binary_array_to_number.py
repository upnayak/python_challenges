def binary_array_to_number(arr):
    return sum([2**x[0] for x in enumerate(arr[::-1]) if x[1] == 1])
