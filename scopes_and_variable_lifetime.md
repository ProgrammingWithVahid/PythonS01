
## Local Scope
```python
def my_function():
    x = 10 # local scope 
    print(x) 

my_function()
# print(x)  # error
```
## Global Scope
```python
x = 50  # global var 

def my_function():
    print(x)

my_function()
print(x)
```
```python
x = 50  # متغیر سراسری

def my_function():
    x = 10  # این یک متغیر محلی جدید است، و x سراسری تغییر نمی‌کند
    print(x)  

my_function()
print(x)  # مقدار اصلی x دست نخورده باقی می‌ماند
```

```python
x = 10  # متغیر سراسری

def my_function():
    global x
    x = 20  # تغییر مقدار متغیر سراسری

my_function()
print(x)  # مقدار x تغییر کرده است
```
## Enclosing or Nonlocal Scope
```python
def outer_function():
    x = 20  # متغیر غیرمحلی

    def inner_function():
        print(x)  # دسترسی به متغیر غیرمحلی
    inner_function()

outer_function()
```

```python
def outer_function():
    x = 20

    def inner_function():
        nonlocal x
        x = 30  # تغییر مقدار متغیر غیرمحلی
    inner_function()
    print(x)  # مقدار x تغییر کرده است

outer_function()
```

## Tipp
### Global-like
```python
x = [10, 20, 30]

def modify_list():
    x.append(40) # it works without global keyword

modify_list()
print(x)  # output: [10, 20, 30, 40]
```
### Variable Shadowing
```python
x = 10  # global var

def my_function():
    x = 5  # new
    print(x)  # output 5

my_function()
print(x)  # output 10

```
