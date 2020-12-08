"""Filter Primes from a List

Create a function that takes a list and returns a new list containing only prime numbers.
Examples

filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]

filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]

filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]

Notes

    New list must maintain the order of primes as they first appear in the original list.
    Check the Resources tab for help."""

def filter_primes(nums):
    return [num for num in nums if is_prime(num)]


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False

if __name__ == '__main__':
    assert filter_primes([7, 9, 3, 9, 10, 11, 27]) == [7, 3, 11]

    assert filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) == [10007, 1009]

    assert filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) == [1009, 3, 61, 1087, 1091, 1093, 1097]


