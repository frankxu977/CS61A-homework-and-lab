
### 1.2   Elements of Programming

- **primitive expressions and statements**, which represent the simplest building blocks that the language provides,
- **means of combination**, by which compound elements are built from simpler ones, and
- **means of abstraction**, by which compound elements can be named and manipulated as units.

### 1.2.2   Call Expressions

The most important kind of compound expression is a _call expression_, which applies a function to some arguments.

There is no limit (in principle) to the depth of such nesting and to the overall complexity of the expressions that the Python interpreter can evaluate.

### 1.2.3   Importing Library Functions

An import statement designates a module name (e.g., operator or math), and then lists the named attributes of that module to import (e.g., sqrt). Once a function is imported, it can be called multiple times.

### 1.2.4   Names and the Environment

A critical aspect of a programming language is the means it provides for using names to refer to computational objects. If a value has been given a name, we say that the name _binds_ to the value.

In Python, names are often called ==_variable names_ or _variables_== because they can be bound to different values in the course of executing a program. When a name is bound to a new value through assignment, it is ==no longer bound to any previous value.== One can even bind built-in names to new values.

### 1.2.5   Evaluating Nested Expressions
![[Pasted image 20251027164222.png]]


### 1.2.6   The Non-Pure Print Function

**Pure functions.** Functions have some input (their arguments) and return some output (the result of applying them). The built-in function

**Non-pure functions.** In addition to returning a value, applying a non-pure function can generate _side effects_, which make some change to the state of the interpreter or computer. A common side effect is to generate additional output beyond the return value, using the print function.

### 1.3   Defining New Functions
**How to define a function.** Function definitions consist of a def statement that indicates a <name> and a comma-separated list of named <formal parameters>, then a return statement, called the function body, that specifies the <return expression> of the function, which is an expression to be evaluated whenever the function is applied:



An environment in which an expression is evaluated consists of a sequence of _frames_, depicted as boxes.Each frame contains _bindings_, each of which associates a name with its corresponding value. There is a single _global_ frame. Assignment and import statements add entries to the first frame of the current environment. So far, our environment consists only of the global frame.


the meaning of a function should be independent of the parameter names chosen by its author

