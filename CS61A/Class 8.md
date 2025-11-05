
1 order of recursive calls

```python

def cascade(x):
	if n<10:
		print(n)
	else:
		print(n)
		cascade(n//10)
		# happen before print(n)
		print(n)
		
		

123
12
1
12
123
```
![[Pasted image 20251103093637.png]]
```python

def inverse_cascade(n):
	grow(n)
	print(n)
	shrink(n)
	
def f_then_g(f,g,n):
	if n：
		f(n)
		g(n)
		
grow= lambda n: f_then_g(grow,print,n//10)
shrink= lambda n: f_then_g(print,shrink,n//10)

```

2 Tree Recursion

```python

def fib(n):
	 if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-2)+fib(n-1)

```
![[Pasted image 20251103094407.png]]

repetition in tree-recursive computation 


2 counting partitions 
![[Pasted image 20251103095421.png]]
好的，这张图（`image.png` 的内容）是在解释一个叫做 **“整数分拆”** 的数学概念，并用一个具体例子说明了递归的计数过程。

---

### 🧩 核心概念解释

**问题**：计算将正整数 `n` 拆分成不超过 `m` 的正整数之和的分拆数量（分拆顺序视为相同，即不考虑顺序）。

在你的例子中：
- \( n = 6 \)（要拆分的整数）
- \( m = 4 \)（使用的最大部分）

函数 **`count_partitions(6, 4)`** 就是计算“把 6 拆分成最大部分不超过 4 的有序分拆”的数量。

---

### 📋 图中列出的所有分拆方式

图中列出了所有 **`count_partitions(6, 4)`** 的结果，也就是所有使用数字 1~4 来组成 6 的方式（顺序不重要，且按非递减顺序列出）：

1.  \( 2 + 4 = 6 \)
2.  \( 1 + 1 + 4 = 6 \)
3.  \( 3 + 3 = 6 \)
4.  \( 1 + 2 + 3 = 6 \)
5.  \( 1 + 1 + 1 + 3 = 6 \)
6.  \( 2 + 2 + 2 = 6 \)
7.  \( 1 + 1 + 2 + 2 = 6 \)
8.  \( 1 + 1 + 1 + 1 + 2 = 6 \)
9.  \( 1 + 1 + 1 + 1 + 1 + 1 = 6 \)

**所以答案是 9 种**。

---

### 🧠 背后的递归思想（通常的实现逻辑）

这个计数过程通常用递归函数来理解：

**定义**：`count_partitions(n, m)`  
- **基准情况**：
  1.  如果 `n == 0`，正好分完，算 **1 种**方法（什么都不用）。
  2.  如果 `n < 0` 或 `m == 0`，无法拆分，算 **0 种**方法。
- **递归情况**：
  分拆方式可以分为 **两大类**：
  1.  **不使用 m 作为部分**：所有部分都 ≤ \( m-1 \)，即 `count_partitions(n, m-1)`。
  2.  **使用至少一个 m 作为部分**：先拿出一个 `m`，剩下的 \( n-m \) 仍然可以用 ≤ \( m \) 的部分来拆分，即 `count_partitions(n-m, m)`。

---

### 🔢 用例子验证递归逻辑

计算 `count_partitions(6, 4)`：

- 不用 4：`count_partitions(6, 3)`（只用 1,2,3）
- 用 4：`count_partitions(2, 4)`（用了 4，剩下 2 用 ≤4 的数字拆分）

然后继续递归下去，最终会得到 9。

![[Pasted image 20251103100334.png]]
```python

def count_partitions(n,m):
	if n==0:
		return 1
	elif n<0:
		return 0
	elif m==0:
		return 0
	else:
		with_m=count_partitions(n-m,m)
		without_m=count_partitions(n,m-1)
		return with_m + without_m

result = count_partitions(5,3)

```