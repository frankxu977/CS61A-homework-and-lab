## What Would Python Display?

> **Important:** For all WWPD questions, type `Function` if you believe the answer is `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.
> 
> 
> **答题格式要求：**

- 如果是函数对象：回答 `Function`
    
- 如果会报错：回答 `Error`
    
- 如果没有输出：回答 `Nothing`
    
- 否则给出具体的输出值
### Q1: WWPD: The Truth Will Prevail

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
> 
> ```
> python3 ok -q short-circuit -u
> ```
> 
>Q1: 短路运算 (Short-circuit)

- `and`: 如果第一个值为真，返回第二个值；否则返回第一个值
    
- `or`: 如果第一个值为真，返回第一个值；否则返回第二个值
    
- `not`: 返回布尔值的相反值

```
>>> True and 13
13
>>> False or 0
0
>>> not 10
False
>>> not None
True
```

```
>>> True and 1 / 0
Error
>>> True or 1 / 0
True
>>> -1 and 1 > 0
1>0
>>> -1 or 5
-1
>>> (1 + 1) and 1
1
>>> print(3) or ""
3
“”
```

```
>>> def f(x):
...     if x == 0:
...         return "zero"
...     elif x > 0:
...         return "positive"
...     else:
...         return ""
>>> 0 or f(1)
positive
>>> f(0) or f(-1)
zero
>>> f(0) and f(-1)
“”
```

### Q2: WWPD: Higher-Order Functions

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
> 
> ```
> python3 ok -q hof-wwpd -u
> ```
> 
>   

```pyhton
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
beets
>>> chocolate
Function
>>> chocolate()
sweets
>>> more_chocolate, more_cake = chocolate(), cake
sweets，cake
>>> more_chocolate
cake


>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
chocolate
>>> snake(10, 20)()
sweets，cake

>>> cake = 'cake'
>>> snake(10, 20)
20+10=30

```

### Q3: WWPD: Lambda

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
> 
> ```
> python3 ok -q lambda -u
> ```
> 
>   
>   
> As a reminder, the following two lines of code will not display any output in the interactive Python interpreter when executed:
> 
> ```
> >>> x = None
> >>> x
> >>>
> ```

```
>>> lambda x: x  # A lambda expression with one parameter x
Function
>>> a = lambda x: x  # Assigning the lambda function to the name a
>>> a(5)
5
>>> (lambda: 3)()  # Using a lambda expression as an operator in a call expression.
3

>>> b = lambda x, y: lambda: x + y  # Lambdas can return other lambdas!
>>> c = b(8, 4)
>>> c
Function
>>> c()
12

>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
16
```

```
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?
Error

>>> higher_order_lambda(g)(2)
4

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
3

>>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
>>> print_lambd
Function

>>> one_thousand = print_lambda(1000)
None



>>> one_thousand # What did the call to print_lambda return?

```

## Coding Practice

### Q4: Composite Identity Function

Write a function that takes in two single-argument functions, `f` and `g`, and returns another **function** that has a single parameter `x`. The returned function should return `True` if `f(g(x))` is equal to `g(f(x))` and `False` otherwise. You can assume the output of `g(x)` is a valid input for `f` and vice versa.

```
def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one) # 赋值给他了一个function
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q composite_identity
```


```python
def composite_identity(f,g):
	def comparison(x):
		if f(g(x))==g(f(x)):
			return True
		else:
			return False
	return comparison

```



### Q5: Count Cond

Consider the following implementations of `count_fives` and `count_primes` which use the `sum_digits` and `is_prime` functions, which are implemented below:

```
def count_fives(n):
    """Return the number of values i from 1 to n (including n)
    where sum_digits(n * i) is 5.

    >>> count_fives(10)  # Among 10, 20, 30, ..., 100, only 50 (10 * 5) has digit sum 5
    1
    >>> count_fives(50)  # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4
    """
    i = 1
    count = 0
    while i <= n:
        if sum_digits(n * i) == 5:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.

    >>> count_primes(6)   # 2, 3, 5
    3
    >>> count_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count
```

The implementations look quite similar! Generalize this logic by writing a function `count_cond`, which takes in a two-argument predicate function `condition(n, i)`. `count_cond` returns a one-argument function that takes in `n`, which counts all the numbers from 1 to `n` that satisfy `condition` when called.

> **Note:** When we say `condition` is a predicate function, we mean that it is a function that will return `True` or `False`.

```
def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    """Return whether positive integer n is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to n that satisfy the two-argument predicate function Condition, where
    the first argument for condition is n and the second argument is the
    number from 1 to n.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q count_cond
```


```python
def count_cond(condition):
    def count_function(n):
        count = 0
        i = 1
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return count_function


```