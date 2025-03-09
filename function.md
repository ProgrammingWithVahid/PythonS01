# Function

```python
def function_name(parameters):  
    #function body
    return value  # مقدار خروجی (اختیاری)
```
#### `def` → برای تعریف تابع
#### `function_name` → نام تابع
#### `parameters` → مقادیر ورودی (اختیاری)
#### `return` → مقدار خروجی تابع (اختیاری)

### تابع بدون ورودی و خروجی
```python
def greet():
    print("Hi there!")

greet()  # فراخوانی تابع
```
### تابع با ورودی و خروجی (return)
```python
def add(a, b):
    result = a + b
    return result  # مقدار جمع را برمی‌گرداند

sum_result = add(5, 10)
print(sum_result)
```

### Default Parameters
```python
def greet(name="user"):
    print(f"hi {name}!")

greet()       # hi user!
greet("vahid")  # hi vahid!
```
### تعداد نامحدود ورودی (*args)
```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15
```
### تعداد نامحدود ورودی کلیدی (**kwargs)
```python
def user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

user_info(name="vahid", age=25, city="tehran")
```
##  توابع بازگشتی (Recursive Functions)
### فاکتوریل عدد!
#### n!=n×(n−1)×(n−2)×...×1
```python
def factorial(n):
    if n == 1:  # شرط توقف (Base Case)
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # output: 120


factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1  (stop condition!)
```
### دنباله فیبوناچی
#### F(n)=F(n−1)+F(n−2)
#### F(0)=0,F(1)=1
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)  # Recursive

print(fibonacci(6))  # output: 8

############################### 10 time faster with 'Decorator'
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # بدون تاخیر محاسبه می‌شود!
```

## تابع به عنوان آرگومان (Higher-Order Function)

```python
def greet():
    print("Hi!")

def before_and_after(func):
    print("Before!")
    func() 
    print("after!")

before_and_after(greet)
```

```python
def square(x):
    return x ** 2

def apply_function(func, value):
    return func(value)

print(apply_function(square, 4))  # output: 16
```
#### تابعی که چند تابع مختلف را اجرا می‌کند
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply_operation(func, x, y):
    return func(x, y)

print(apply_operation(add, 5, 3))       # output: 8
print(apply_operation(multiply, 5, 3))  # output: 15
```
#### تابعی که خودش یک تابع جدید برمی‌گرداند!
```python
def make_multiplier(n):
    def multiplier(x):
        return x * n 
    return multiplier 

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # output: 10
print(triple(5))  # output: 15
```

```python
```

```python
```

```python
```
