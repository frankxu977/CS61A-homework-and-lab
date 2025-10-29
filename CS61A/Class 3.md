
1 The Fibonacci Sequence 

consider: 
1 index and number 
2 what information you need to focus on?
![[Pasted image 20251029173348.png]]
key point=pred+curr=new 


2 control statement : if and while 

clause---header---skip or execute---
(not do both)

![[Pasted image 20251029174009.png]]
```
if_(x>=0,sqrt(x),0)
# 报错：先计算了sqrt（x）

def if_(c,t,f):
	if x>=0:
		return sqrt(x)
	else:
		0
```

3 logical operator 
	 1 a and b 再 a不成立的时候就不会计算b了
	 2 a or b    

4 high order function 

![[Pasted image 20251029175303.png]]
```
from math import pi, sqrt

def area(r,shape_constant):
	assert r>0,
	return r*r*shape_constant

def area_square(r):
	assert r>0,
	return area(r,1)

def area_circle(r):
	return area(r,pi)
	
def area_hexagon(r):
	return area(r,3*sqrt(3)/2)
	
assert 3>2 , "math is broken"
assert 2>3 , "that is false"
```
![[Pasted image 20251029180002.png]]

```
def sum_naturals(n):
	total,k=0,1
	while k<=n:
		total,k=total+k, k+1
	return total

def sum_cubes(n):
	total,k=0,1
	while k<=n:
		total,k=total+pow(k,3),k+1
	return total 
	
# not need to repeat 

def identity(k):
	return k
	
def cube(k):
	return pow(k,3)
	
def summation (n,term):
	total,k=0,1
	while k<=n:
		total,k=total+term(k),k+1
	return total 
	
	
def sum_naturals(n):
	return summation(n,identity)

def sum_cubes(n):
	return summation(n,cube)
```
avoid to doing repeating things 


function as a return value :
![[Pasted image 20251029181453.png]]
![[Pasted image 20251029181546.png]]

好的！我用一个非常简单的例子来彻底解释柯里化是什么意思。

---

## 🍪 用一个"做三明治"的比喻来解释

想象你要做一个三明治，需要三个步骤：
1. 拿面包
2. 加馅料  
3. 合上面包

### 普通做法（非柯里化）
```python
def make_sandwich(bread, filling, close):
    return f"{bread} + {filling} + {close} = 三明治完成！"

# 一次性提供所有材料
result = make_sandwich("🍞", "🥬", "🍞")
print(result)  # 输出: 🍞 + 🥬 + 🍞 = 三明治完成！
```

### 柯里化做法
```python
def curried_sandwich(bread1):
    def add_filling(filling):
        def add_top(bread2):
            return f"{bread1} + {filling} + {bread2} = 三明治完成！"
        return add_top
    return add_filling

# 分步骤做三明治
step1 = curried_sandwich("🍞")      # 先拿一片面包
step2 = step1("🥓")                 # 再加培根馅料
step3 = step2("🍞")                 # 最后盖上另一片面包
print(step3)  # 输出: 🍞 + 🥓 + 🍞 = 三明治完成！
```

---

## 🔍 柯里化的核心思想

### 把 **一次调用多个参数**：
```python
函数(参数1, 参数2, 参数3)
```

### 变成 **多次调用，每次一个参数**：
```python
函数(参数1)(参数2)(参数3)
```

---

## 💡 为什么要这样？有什么好处？

### 好处1：创建专用函数
```python
# 先固定面包类型
wheat_bread_sandwich = curried_sandwich("全麦🍞")

# 用同样的面包做不同馅料的三明治
ham_sandwich = wheat_bread_sandwich("火腿")("全麦🍞")
veggie_sandwich = wheat_bread_sandwich("蔬菜")("全麦🍞")

print(ham_sandwich)    # 全麦🍞 + 火腿 + 全麦🍞 = 三明治完成！
print(veggie_sandwich) # 全麦🍞 + 蔬菜 + 全麦🍞 = 三明治完成！
```

### 好处2：延迟执行
```python
# 先准备一部分
first_step = curried_sandwich("🍞")  # 拿了面包，但还不做完整三明治

# 稍后决定加什么馅料
later_decision = first_step("🍗")("🍞")  # 现在才完成三明治
```

### 好处3：代码复用
```python
# 创建"标准汉堡"模板
standard_burger = curried_sandwich("汉堡🍞") 

# 快速制作不同口味的汉堡
cheese_burger = standard_burger("奶酪")("汉堡🍞")
chicken_burger = standard_burger("鸡肉")("汉堡🍞")
```

---

## 🎯 实际编程例子

```python
# 普通函数 - 计算折扣价格
def calculate_discount(price, discount_rate, tax_rate):
    discounted = price * (1 - discount_rate)
    return discounted * (1 + tax_rate)

# 柯里化版本
def curried_discount(price):
    def apply_discount(discount_rate):
        def apply_tax(tax_rate):
            discounted = price * (1 - discount_rate)
            return discounted * (1 + tax_rate)
        return apply_tax
    return apply_discount

# 创建"9折优惠"的专用计算器
nine_discount = curried_discount(100)(0.1)  # 固定商品100元，打9折

# 在不同税率的地区使用
result_ny = nine_discount(0.08)  # 纽约8%税
result_ca = nine_discount(0.09)  # 加州9%税

print(f"纽约价格: {result_ny}")  # 纽约价格: 106.92
print(f"加州价格: {result_ca}")  # 加州价格: 107.91
```

---

## ✅ 总结

**柯里化就是：**
- 🔄 **转换调用方式**：`f(a,b,c)` → `f(a)(b)(c)`
- 🎯 **固定部分参数**：先提供一些参数，创建更专用的函数
- ⏰ **延迟执行**：可以分阶段提供参数，需要时才最终计算
- 🔧 **提高复用**：通过固定某些参数，创建可重用的函数模板

**简单说：柯里化让你像"组装乐高"一样组合函数，而不是一次性完成所有工作！**

