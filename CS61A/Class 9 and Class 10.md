
1 List

```python

digit=[1,2,3,4,5,6,7,8,9,10]

len()

digit[3]

digits*2+[]

```

2 containers 

```python

digits=[1,2,3,4]
1 in digits 
8 in digits 
5 not in digits 

# one elements at a time 

```

3 for statements 

```python
def count(s,value):
	total,index=0,0
	while index<len(S):
		element=s[index]
		
		if element==value:
			total+=1
		
		index+=1
		
	return total 
	
def second_total(s,value)：
	total=0
	for element in s:
		if element==value:
			total+=1
	return total
	

```

4 sequence iteration

sequence unpacking in for statements 

![[Pasted image 20251105103741.png]]


5 ranges

a sequence of consecutive integers 

![[Pasted image 20251105104004.png]]

```python

def sum_below(n):
	total=0
	for i in range(n):
		total+=1
	return total 
	
def cheer():
	for _ in range(3):
		print("hello world")

```


6 list comprehensions 
```python

odds=[1,3,5,7,9]
[x+1 for x in odds]
[x for x in odds if 25%x==0]
[x+1 for x in odds if 25%x==0]



```
