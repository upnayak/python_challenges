"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors
(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime'

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

"""


def divisors(integer):
    assert integer > 1, "Integer is not greater then 1"
    divisor_list = [x for x in range(1, integer+1) if integer % x == 0]
    if len(divisor_list) == 2:
        return '{} is prime'.format(integer)
    divisor_list.pop(0)
    divisor_list.pop(-1)
    return divisor_list
