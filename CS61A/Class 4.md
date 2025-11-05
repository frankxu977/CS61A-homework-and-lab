
1 high order function 

a function that takes a function as an environment as argument or returns a function 

```python

def apply_twice(f,x):
	return f(f(x))
	
def square(x):
	return x*x 


```


2 environment for nested environment 

```python

def make_adder(n):
	def adder(k):
		return k+n
	return adder 
	
add_three=make_adder(3)
add_three(4)

```

这个环境图展示了 **嵌套函数（nested function）** 和 **父帧（parent frame）** 的运行方式，我来一步步解释。

---

## 1. 代码结构

```python
def make_adder(n):
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
result = add_three(4)  # 结果是 7
```

---

## 2. 环境帧（frame）与父帧（parent）

### **Global 帧**
- 有变量：
  - `make_adder`：函数对象，其父帧是 Global
  - `add_three`：是 `make_adder(3)` 的返回值，即一个 `adder` 函数实例

---

### **f1: make_adder 调用帧**
- 当执行 `make_adder(3)` 时创建
- 局部变量：
  - `n` → 3
  - `adder` → 一个函数对象，其 **父帧是 f1**（不是 Global）
- ==返回 `adder` 函数==

---

### **f2: adder 调用帧**
- 当执行 `add_three(4)` 时创建
- 参数：
  - `k` → 4
- 需要计算 `k + n`，但 `n` 不在 f2 中
- ==**查找规则**：如果当前帧没有变量 `n`，就去它的 **父帧（parent frame）** 中找==
- ==父帧是 **f1**，在 f1 中找到 `n` 为 3==
- 计算 `4 + 3` → 7

---

## 3. 关键概念：闭包（Closure）

- `adder` 函数记住了它定义时的环境（f1 帧），即使 `make_adder` 已经执行完毕并返回
- 这种“函数 + 定义环境”称为 **闭包**
- 每次调用 `make_adder` 会创建不同的父帧，因此返回的 `adder` 函数会绑定不同的 `n`

![[Pasted image 20251030140449.png]]

3 how to draw an environment diagram 
![[Pasted image 20251030141025.png]]

4 local name

![[Pasted image 20251030141320.png]]

5 function composition

```python
def square(x):
	return x*x

def triple(x):
	return 3*x

def compsel(f,g):
	def h(x):
		return f(g(x))
	return h 
	
composel(square,make_adder(2))(3)

```

6 lambda expression

```python
square=lambda x:x*x
# no return key words

```
![[Pasted image 20251030142923.png]]

7 function currying 柯里化

```python
def mae_adder(n):
	return lambda k:n+k



```
![[Pasted image 20251030143430.png]]
