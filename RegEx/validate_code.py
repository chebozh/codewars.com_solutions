"""
Basic regex tasks. Write a function that takes in a numeric code of any length.
The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.

You can assume the input will always be a number.

8kuy
"""
import re


def validate_code(code):
    return bool(re.match(r'[123]', str(code)))


# examples
print(validate_code(123))
print(validate_code(248))
print(validate_code(8))
print(validate_code(321))
print(validate_code(9453))
