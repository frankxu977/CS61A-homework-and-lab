1 self reference

```python
def print_all(x):
	print(x)
	return print_all
	
print_all(1)(3)(5)

def print_all(x):
	print(x)
	def next_sum(y):
		return print_sums(x+y)
	return next_sum
 
```

2 definition of recursive functions

if the body of that function calls itself, either directly or indirectly

```python
def split(n):
	return n//10,n%10
	
def sum_digits(n):
	if n<10:
		return n
	else:
		all_but_last,last=split(n)
		return sum_digits(all_but_last)+last
		

```

3 recursion in environment diagrams

![[Pasted image 20251102183657.png]]

4 iteration vs recursion 

![[Pasted image 20251102183912.png]]
1 recursion is easier to read 

2 recursion has less names ( only n fact  )


5 verifying recursive function 


```python
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)

1 verify the base case
2 treat fact as a functional abstraction 
3 assume that fact(n-1) is coorect
4 verify that fact(n) is correct 

数学归纳法

```

6 mutual recursion

![[Pasted image 20251102184833.png]]

隔一个两倍

一个数位不对 他的和就是不是10的倍数

```python
def luh_sum(n):
	if n<10:
		return n
	else:
		all_but_last,last=split(n)
		return luhn_sum_double(all_but_last)+last
		
def luhn_sum double(n):
	all_but_last,last=split(n)
	luhn_digit=sum_digits(2*last)
	if n<10:
		return luhn_digit
	else：
		return luhn_sum(all_but_las)+luhn_digit

```

![[Pasted image 20251102185814.png]]
