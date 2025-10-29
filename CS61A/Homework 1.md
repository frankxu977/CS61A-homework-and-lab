```python
### Q1: Product

Write a function called `product` that returns the product of the first `n` terms of a sequence. Specifically, `product` takes in an integer `n` and `term`, a single-argument function that determines a sequence. (That is, `term(i)` gives the `i`th term of the sequence.) `product(n, term)` should return `term(1) * ... * term(n)`
def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term: a function that takes an index as input and produces a term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
```

```python
def identity(k):
	return k
	
def square(k):
	return pow(k,2)
	
def increment(k):
	return k+1

def triple(k):
	return 3*k
	
def product(n,term):
	total,k=1,1
	while k<=n:
		total,k=total*term(k),k+1
	return total 
```

### Q2: Accumulate

Let's take a look at how `product` is an instance of a more general function called `accumulate`, which we would like to implement:

```
def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    "*** YOUR CODE HERE ***"
```

`accumulate` has the following parameters:

- `fuse`: a two-argument function that specifies how the current term is fused with the previously accumulated terms
- `start`: value at which to start the accumulation
- `n`: a non-negative integer indicating the number of terms to fuse
- `term`: a single-argument function; `term(i)` is the `i`th term of the sequence

Implement `accumulate`, which fuses the first `n` terms of the sequence defined by `term` with the `start` value using the `fuse` function.

For example, the result of `accumulate(add, 11, 3, square)` is

```
add(11,  add(square(1), add(square(2),  square(3)))) =
    11 +     square(1) +    square(2) + square(3)    =
    11 +     1         +    4         + 9            = 25
```

> Assume that `fuse` is commutative, `fuse(a, b) == fuse(b, a)`, and associative, `fuse(fuse(a, b), c) == fuse(a, fuse(b, c))`.


```python
def identity(k):
	return k

def square(k):
	return pow(k,2)
	
def accumulate(fuse,start,n,term):
	total,k=start,1
	while k<=n:
		total,k=fuse(total,term(k)),k+1
	return total 
	
```

### Q3: Make Repeater

Implement the function `make_repeater` which takes a one-argument function `f` and a positive integer `n`. It returns a one-argument function so that `make_repeater(f, n)(x)` returns the value of `f(f(...f(x)...))`, in which `f` is applied `n` times to `x`. For example, `make_repeater(square, 3)(5)` squares 5 three times and returns 390625, just like `square(square(square(5)))`.

```
def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q make_repeater
```

```python
def make_repeater(f,n):
	def number(k):
		result=k
		for _ in range(n):
			result=f(result)
		return result
	return number
	
	
这个实现巧妙地利用了：

- **闭包**来记住参数
    
- **循环**来重复应用函数
    
- **高阶函数**来创建新的函数行为

```