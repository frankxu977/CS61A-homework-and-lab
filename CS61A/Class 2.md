1 def statement= name + body + return statement 
2 call expression 
3 calling/applying 


Multiple Environments in one Diagram 
example: square(square(3))
![[Pasted image 20251028084225.png]]
an environment is a sequence of frames
1 global frame alone
2 a local . then global frame 

`from operator import truediv,floordive`

return 多个values:

`def divide_exact(n,d):`
	`return n//d , n%d`

`python3 -m doctest ex.py`


A statement is executed by the interpreter to perform an action

statement=clause+suite
![[Pasted image 20251028091334.png]]

这是一个关于 Python **条件语句结构**的说明。让我来解释这些术语：

## 代码结构分析

```python
def absolute_value(x):
    """Return the absolute value of x."""
    if x < 0:        # Header 1
        return -x    # Suite 1
    elif x == 0:     # Header 2  
        return 0     # Suite 2
    else:            # Header 3
        return x     # Suite 3
```

## 术语解释

### 1. Statement（语句）
- **整个 `if-elif-else` 结构**是一个条件语句
- 这是一个完整的逻辑单元

### 2. Clauses（子句）- 2个
- `if` 子句
- `elif` 子句
- `else` 不算独立的子句，它依附于前面的条件

### 3. Headers（头部）- 3个
每个条件判断的部分：
```python
if x < 0:     # Header 1
elif x == 0:  # Header 2  
else:         # Header 3
```

### 4. Suites（代码块）- 3个
每个条件对应的执行代码：
```python
return -x  # Suite 1 (对应 if)
return 0   # Suite 2 (对应 elif)
return x   # Suite 3 (对应 else)
```

## 可视化结构

```
if x < 0:        ← Header 1
    return -x    ← Suite 1
elif x == 0:     ← Header 2  
    return 0     ← Suite 2
else:            ← Header 3
    return x     ← Suite 3
```

## 总结
- **1个 Statement**：完整的条件结构
- **2个 Clauses**：if 和 elif 子句
- **3个 Headers**：所有条件判断行
- **3个 Suites**：所有对应的代码块

这样分解有助于理解 Python 条件语句的语法结构！