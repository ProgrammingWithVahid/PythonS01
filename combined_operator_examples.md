# 🎯 20 Combined Operator Examples in Python  


اوپراتورهای محاسباتی# (Arithmetic Operators) 
```+ - * / // % **```
اوپراتورهای مقایسه‌ای (Comparison Operators) 
== != < > =< =>
اوپراتورهای منطقی (Logical Operators)
and or not
اوپراتورهای انتساب (Assignment Operators)
= += -= *= /= //= %= =**
اوپراتورهای عضویت (Membership Operators)
in   not in
اوپراتورهای بیتی (Bitwise Operators) 
& | ^ ~ << >> 




# 1. Arithmetic and Comparison Operators  
```python
a = 5
b = 3
c = 2
result = (a + b * c) > (a - b / c)
print(result)  # True
```
# 2. Logical and Comparison Operators
```python
age = 25
is_member = True
result = (age > 18 and age < 60) or is_member
print(result)  # True
```
# 3. Compound Assignment with Arithmetic
```python
x = 10
x += 5 * 2  # Equivalent to: x = x + (5 * 2)
print(x)  # 20
```
# 4. Using `not` with Comparison and Logical Operators
```python
is_admin = False
age = 30
result = not is_admin and age > 18
print(result)  # True
```
# 5. Combining `in` and `not` with Comparison
```python
users = ["alice", "bob", "charlie"]
user = "dave"
result = user not in users and len(user) > 3
print(result)  # True
```
# 6. Using `is` with Logical and Comparison Operators
```python
x = None
y = 0
result = (x is None) or (y == 0)
print(result)  # True
```
# 7. Bitwise with Comparison and Logical
```python
a = 5  # 0101
b = 3  # 0011
result = (a & b) > 0 and (a | b) == 7
print(result)  # True
```
# 8. Bit Shifting with Comparison
```python
num = 8   # 1000
result = (num << 1) == (num * 2) and (num >> 2) == (num // 4)
print(result)  # True
```
# 9. Combining `and`, `or`, and `not`
```python
a = True
b = False
c = True
result = not (a and b) or (b or c)
print(result)  # True
```
# 10. Bitwise and Shift with Assignment
```python
x = 6   # 0110
x <<= 1
x |= 1
print(x)  # 13 (1101)
```
# 11. Using `is not` with Comparison and Logical
```python
value = 10
status = None
result = (value > 5) and (status is not None)
print(result)  # False
```
# 12. Arithmetic, Comparison, and Logical in One Condition
```python
score = 85
attendance = 90
passed = (score > 80 and attendance > 75) or (score > 90)
print(passed)  # True
```
# 13. Bitwise OR with Shift for Flag Setting
```python
flags = 0b0000
READ = 0b0001
WRITE = 0b0010
flags |= (READ | WRITE)
print(bin(flags))  # 0b11
```
# 14. Combining `in`, Comparison, and `and`
```python
password = "secret123"
requirements = len(password) > 8 and any(char.isdigit() for char in password)
print(requirements)  # True
```
# 15. XOR and AND to Check Unique Bits
```python
a = 9   # 1001
b = 5   # 0101
result = (a ^ b) > 0 and (a & b) == 0
print(result)  # True
```
# 16. Shift and XOR for Simple Encryption
```python
key = 7
data = 12
encrypted = (data << 2) ^ key
decrypted = (encrypted ^ key) >> 2
print(decrypted == data)  # True
```
# 17. Using `not in` and `and` in Complex Condition
```python
name = "john"
banned_names = ["admin", "root"]
is_valid = name not in banned_names and len(name) > 3
print(is_valid)  # True
```
# 18. Compound `+=` with Arithmetic and Logical
```python
counter = 0
value = 5
if value > 0 and value < 10:
    counter += value
print(counter)  # 5
```
# 19. Using `is` and `or` for Value or Type Check
```python
data = None
result = (data is None) or (isinstance(data, int) and data > 0)
print(result)  # True
```
# 20. Multiple Operators with Different Precedences
```python
a = 3
b = 4
c = 5
result = (a + b * c) > (c ** a) and ((b | c) == 5)
print(result)  # False
```
