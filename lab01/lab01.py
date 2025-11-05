from re import I


def digit(n, k):
    """Return the k-th digit from the right of n for positive integers n and k.
    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return n//(10**k)%10

def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return max(min(a,b),min(b,c),min(a,c))
   


def falling(n, k):
    result = 1
    for i in range(k+1):
        result = result * (n - i)
    
    return result


def divisible_by_k(n, k):
    count = 0
    for i in range(1, n + 1):
        if i % k == 0:
            print(i)
            count += 1
    return count
   


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    num_str = str(n)
    for i in range(len(num_str) - 1):
        if num_str[i] == '8' and num_str[i + 1] == '8':
            return True
    return False

