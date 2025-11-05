
### 1.6.1   Functions as Arguments
```python

def summation(n, term):
	total, k = 0, 1
	while k <= n:
	total, k = total + term(k), k + 1
	return total

def cube(x):
	return x*x*x

def sum_cubes(n):
	return summation(n, cube)

result = sum_cubes(3)

```
### 1.6.2   Functions as General Methods
some functions express general methods of computation, independent of the particular functions they call

函数不仅可以抽象数值操作，还可以抽象计算过程本身

### **两个计算机科学重要思想**：

1. **抽象**：通过命名和函数隐藏复杂性
    
2. **组合**：通用求值过程让小组件可以组合成复杂过程

```python
# 1. 通用迭代改进框架
def improve(update, close, guess=1):
    """
    通用迭代改进算法
    update: 改进猜测的函数
    close: 判断是否足够接近目标的函数
    guess: 初始猜测值
    """
    while not close(guess):
        guess = update(guess)
    return guess

# 2. 近似相等判断函数
def approx_eq(x, y, tolerance=1e-15):
    """
    判断两个数是否在容差范围内近似相等
    """
    return abs(x - y) < tolerance

# 3. 黄金比例特定的函数
def golden_update(guess):
    """
    根据黄金比例的性质更新猜测值
    φ = 1/φ + 1
    """
    return 1/guess + 1

def square_close_to_successor(guess):
    """
    检查当前猜测是否满足黄金比例的性质
    φ² = φ + 1
    """
    return approx_eq(guess * guess, guess + 1)

# 4. 计算黄金比例
def compute_golden_ratio():
    """
    使用迭代改进方法计算黄金比例
    """
    phi_approx = improve(golden_update, square_close_to_successor)
    return phi_approx

# 5. 测试函数
def improve_test():
    """
    验证计算结果是否正确
    """
    from math import sqrt
    
    # 精确的黄金比例值
    phi_exact = (1 + sqrt(5)) / 2
    
    # 迭代计算得到的近似值
    phi_approx = compute_golden_ratio()
    
    # 验证两者是否足够接近
    assert approx_eq(phi_exact, phi_approx), f'phi differs from its approximation: {phi_exact} vs {phi_approx}'
    
    print("测试通过！")
    print(f"精确值: {phi_exact}")
    print(f"近似值: {phi_approx}")
    print(f"误差: {abs(phi_exact - phi_approx)}")

# 6. 演示迭代过程
def demonstrate_iteration():
    """
    展示迭代过程，帮助理解算法如何收敛
    """
    print("迭代过程演示:")
    guess = 1
    print(f"初始猜测: {guess}")
    
    for i in range(10):
        old_guess = guess
        guess = golden_update(guess)
        error = abs(guess * guess - (guess + 1))
        print(f"第{i+1}次迭代: {guess:.10f}, 误差: {error:.10f}")
        
        if square_close_to_successor(guess):
            print("已收敛到满足精度的解")
            break

# 7. 主程序
if __name__ == "__main__":
    # 计算并显示结果
    phi = compute_golden_ratio()
    print(f"计算得到的黄金比例: {phi}")
    print()
    
    # 演示迭代过程
    demonstrate_iteration()
    print()
    
    # 运行测试
    improve_test()
    print()
    
    # 展示这个框架的通用性
    print("=== 框架通用性演示 ===")
    
    # 用同样的框架计算平方根
    def sqrt_update(guess, x):
        return (guess + x/guess) / 2
    
    def sqrt_close(guess, x):
        return approx_eq(guess * guess, x)
    
    # 计算√2
    sqrt_2 = improve(lambda g: sqrt_update(g, 2), lambda g: sqrt_close(g, 2), guess=1)
    print(f"√2 的近似值: {sqrt_2}")
    print(f"验证: {sqrt_2}² = {sqrt_2 * sqrt_2}")

```

### 1.6.3   Defining Functions III: Nested Definitions

好的，我来用更详细、更通俗的方式解释嵌套函数和词法作用域。让我们一步一步来。

## 1. 先看我们遇到的问题

### **问题1：函数太多，名字冲突**
想象你有一个工具箱，如果所有工具都扔在同一个大箱子里：
- 锤子、螺丝刀、扳手都混在一起
- 找起来很麻烦
- 不能有两个同名的工具

代码中也是这样：
```python
def update1(x): ...  # 用于黄金比例
def update2(x, a): ...  # 用于平方根
def close1(x): ...  # 用于黄金比例  
def close2(x, a): ...  # 用于平方根
```
→ 全局空间很快就被各种小函数填满了

### **问题2：函数签名不匹配**
`improve` 函数要求 `update` 函数只能有一个参数：
```python
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)  # 这里只传一个参数！
    return guess
```

但计算平方根需要两个参数：
```python
def sqrt_update(x, a):  # 需要 x 和 a 两个参数！
    return average(x, a/x)
```
→ 不兼容！

---

## 2. 解决方案：把函数装进"盒子"里

### **就像整理工具箱**
把相关的工具放在一个小盒子里，再把小盒子放在大工具箱里：

```python
def sqrt(a):  # 这是"平方根工具箱"
    
    # 这些是工具箱里的小工具
    def sqrt_update(x):  # 改进猜测的工具
        return average(x, a/x)
    
    def sqrt_close(x):   # 检查精度的工具  
        return approx_eq(x * x, a)
    
    # 使用工具箱里的工具工作
    return improve(sqrt_update, sqrt_close)
```

**好处：**
- 外部看不到 `sqrt_update` 和 `sqrt_close`，不会重名
- `sqrt_update` 只需要一个参数 `x`，符合 `improve` 的要求

---

## 3. 关键魔法：内部函数如何知道 `a` 的值？

这是最神奇的部分！让我们仔细看看：

### **执行过程分解**

**步骤1：调用 `sqrt(256)`**
```python
# 创建 sqrt 的工作空间（帧）
sqrt 的工作台：
    a = 256
    sqrt_update = <函数，记住这个工作台>
    sqrt_close = <函数，记住这个工作台>
```

**步骤2：定义内部函数**
当 Python 看到 `def sqrt_update(x):` 时，它做了一件重要的事：
- 创建 `sqrt_update` 函数
- **让这个函数记住当前的工作台（包含 a=256）**

**步骤3：调用 `improve`**
```python
improve 的工作台：
    update = sqrt_update  # 这个函数记得 a=256
    close = sqrt_close    # 这个函数也记得 a=256  
    guess = 1
```

**步骤4：调用 `sqrt_update(1)`**
```python
# 创建 sqrt_update 的工作台
sqrt_update 的工作台：
    x = 1
    
# 但关键是：这个工作台连接到之前记住的 sqrt 工作台
```

### **名称查找过程**
当 `sqrt_update` 需要计算 `a/x` 时：

1. **在自己的工作台找 a**
   ```
   sqrt_update的工作台：{x: 1} 
   → 没有找到 a
   ```

2. **去连接的工作台找 a**  
   ```
   sqrt的工作台：{a: 256, ...}
   → 找到了！a = 256
   ```

3. **计算结果**
   ```python
   return average(1, 256/1)  # average(1, 256)
   ```

---

## 4. 环境链的可视化

让我们画图理解：

```
第1层：全局环境
   improve, average, approx_eq, sqrt 等函数

第2层：sqrt(256) 调用时
   a = 256
   sqrt_update = <函数，指向第2层>
   sqrt_close = <函数，指向第2层>

第3层：sqrt_update(1) 调用时  
   x = 1
   ↑
   连接到第2层（因为记得定义时的环境）
```

**查找路径**：第3层 → 第2层 → 第1层

---

## 5. 词法作用域 vs 动态作用域

### **词法作用域（Lexical Scoping）** - Python 使用
"你在哪里出生，就继承哪里的环境"

```python
def outer():
    name = "Alice"
    def inner():
        print(name)  # 总是打印 "Alice"，无论在哪调用
    return inner

func = outer()
func()  # 打印 "Alice"，因为 inner 记得它出生时的环境
```

### **动态作用域（某些语言使用）**  
"你在哪里被调用，就使用哪里的环境"

（Python 不是这样工作的）

---

## 6. 闭包的实用例子

### **计数器工厂**
```python
def create_counter():
    count = 0  # 这个变量被"记住"了
    
    def counter():
        nonlocal count  # 告诉Python我们要修改外部变量
        count += 1
        return count
    
    return counter

# 使用
counter1 = create_counter()
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

counter2 = create_counter()  # 新的计数器，独立的count
print(counter2())  # 1
```

### **乘数工厂**
```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor  # 记得 factor 的值
    return multiplier

double = make_multiplier(2)    # 记住 factor=2
triple = make_multiplier(3)    # 记住 factor=3

print(double(5))  # 10 = 5 * 2
print(triple(5))  # 15 = 5 * 3
```

---

## 7. 总结要点

1. **嵌套函数就像小工具放在工具箱里** - 避免全局命名冲突

2. **内部函数记得出生环境** - 即使外部函数执行完毕

3. **名称查找沿环境链向上** - 自己 → 父环境 → 祖父环境 → ... → 全局

4. **闭包 = 函数 + 出生环境** - 让函数"携带数据"

5. **解决了两大问题**：
   - 命名空间污染
   - 函数签名约束

### 1.6.4   Functions as Returned Values
好的，我来详细解释"函数作为返回值"这个概念。这其实是闭包的一个很酷的应用！

## 1. 基本概念：函数制造函数

想象一个"函数工厂"：你给它一些原料，它给你生产一个新的函数。

```python
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h  # 返回一个新制造的函数！
```

---

## 2. 具体例子：组合两个函数

### **我们有两个简单函数**
```python
def square(x):
    return x * x

def successor(x):
    return x + 1
```

### **我们想要组合它们**
数学上：`h(x) = square(successor(x))`

用代码：
```python
# 方法1：直接写
def square_successor(x):
    return square(successor(x))

# 方法2：用 compose1（更通用）
square_successor = compose1(square, successor)
```

---

## 3. 执行过程详解

让我们一步步跟踪 `square_successor = compose1(square, successor)`：

### **步骤1：调用 compose1**
```python
# 创建 compose1 的工作台
compose1 的工作台：
    f = square函数
    g = successor函数 
    h = <新函数，记得这个工作台>
    
返回：h函数（记得f=square, g=successor）
```

### **步骤2：调用 square_successor(12)**
实际上就是调用 `h(12)`：

```python
# 创建 h 的工作台
h 的工作台：
    x = 12
    
# 但h记得它的出生环境（compose1的工作台）
```

### **步骤3：执行 h 的函数体**
`return f(g(x))` 分解执行：

1. **计算 g(x)**
   ```python
   g(x) = successor(12) = 13
   ```

2. **计算 f(结果)**
   ```python
   f(13) = square(13) = 169
   ```

3. **返回 169**

---

## 4. 为什么这很神奇？看看名称解析

注意！全局环境中还有一个叫 `f` 的函数：
```python
def f(x):
    return -x  # 这个函数永远不会被调用！
```

但是当 `h` 查找 `f` 时：

1. **在 h 的工作台找 f** → 没找到
2. **去父环境（compose1工作台）找 f** → 找到了！`f = square函数`

**关键**：`h` 使用的是它**定义时**的 `f` 和 `g`，不是调用时的！

---

## 5. 环境图分析

```
全局环境：
    square: <函数>
    successor: <函数> 
    compose1: <函数>
    f: <返回-x的函数> ← 这个f不会被用到！
    square_successor: <h函数>

f1: compose1调用时 [父环境=全局]
    f: square函数     ← h记住的是这个f！
    g: successor函数  ← h记住的是这个g！
    h: <函数，父环境=f1>

f2: h调用时 [父环境=f1]  
    x: 12
    → 查找f：在f1中找到square
    → 查找g：在f1中找到successor
```

---

## 6. 更多的实用例子

### **函数工厂**
```python
def make_power_function(exponent):
    """制造一个计算x的n次方的函数"""
    def power(x):
        return x ** exponent
    return power

# 使用工厂
square = make_power_function(2)      # 制造平方函数
cube = make_power_function(3)        # 制造立方函数
sqrt = make_power_function(0.5)      # 制造平方根函数

print(square(5))    # 25
print(cube(3))      # 27  
print(sqrt(16))     # 4.0
```

### **带配置的函数**
```python
def make_greeter(greeting, punctuation):
    """制造一个打招呼的函数"""
    def greet(name):
        return f"{greeting}, {name}{punctuation}"
    return greet

hello = make_greeter("Hello", "!")
hi = make_greeter("Hi", "~")
formal = make_greeter("Good day", ".")

print(hello("Alice"))    # "Hello, Alice!"
print(hi("Bob"))         # "Hi, Bob~"
print(formal("Charlie")) # "Good day, Charlie."
```

---

## 7. 为什么这很有用？

### **1. 代码复用**
```python
# 不用为每个组合写新函数
square_successor = compose1(square, successor)
double_successor = compose1(lambda x: 2*x, successor)
# ... 无限组合
```

### **2. 配置化**
一次配置，多次使用：
```python
logger = make_logger(level="INFO", format="json")
# 之后一直用这个配置好的logger
```

### **3. 状态封装**
```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# 每个计数器都有自己的独立状态
c1 = make_counter()
c2 = make_counter()
```

---

## 8. 关键理解点

1. **函数可以像值一样返回**
2. **返回的函数记得它的出生环境**
3. **名称解析基于定义时，不是调用时**
4. **不需要修改环境模型** - 这是我们之前学的作用域规则的自然延伸
