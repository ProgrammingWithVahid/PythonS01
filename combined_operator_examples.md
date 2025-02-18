# Operator in Python  
### Arithmetic Operators(اوپراتورهای محاسباتی)    ```+ - * / // % **```
### Comparison Operators(اوپراتورهای مقایسه‌ای)    ```== != < > =< =>```
### Logical Operators(اوپراتورهای منطقی)         ```and or not```
### Assignment Operators(اوپراتورهای انتساب)      ```= += -= *= /= //= %= =**```
### Membership Operators(اوپراتورهای عضویت)     ```in   not in```
### Identity Comparison                     ```is is not```
### ```is None```
### Bitwise Operators(اوپراتورهای بیتی)           ```& | ^ ~ << >>```


## Logical Operators
```
a = True 
b = False 
print(a and b) # False 
print(not a) # False

a = 5
b = 10
print(a > 0 and b > 0) # True (هر دو شرط درست هستند)
print(a > 0 and b < 0) # False (شرط دوم غلط است)
```
### and
```
True  True        True
True  False       False
False True        False
False False       False
```
نکته: در and اگر شرط اول غلط باشد، شرط دوم اصلاً بررسی نمی‌شود (چون نتیجه به‌هرحال False است). این ویژگی به‌نام Short-Circuit Evaluation شناخته می‌شود.
### or
```
True  True        True
True  False       True
False True        True
False False       False
```
### not
```
True    False
False   True
```
نکته: not اولویت بیشتری نسبت به and و or دارد. پس در عبارات پیچیده، ابتدا شرط درون not ارزیابی می‌شود.

در پایتون، مقادیر زیر به‌عنوان False درنظر گرفته می‌شوند:
```

None
False
0
"" (رشته خالی)
[], (), {} (لیست، تاپل، یا دیکشنری خالی)

name = ""
print(not name)  # True چون رشته خالی است
```
## Assignment Operators
x = 5
x += 3   # معادل x = x + 3
print(x) # 8

## Membership Operators
```python
lst = [1, 2, 3]
print(2 in lst)      # True
print(4 not in lst)  # True
```

## Identity Operators
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)   # True (مقدارها برابرند)
print(a is b)   # False (هویت‌ها متفاوتند)
print(a is c)  # True  -> چون به همان مکان حافظه اشاره می‌کنند

x = 256
y = 256
print(x is y)  # True -> چون اعداد کوچک در حافظه مشترک هستند

x = 257
y = 257
print(x is y)  # False -> چون اعداد بزرگ‌تر از 256 در مکان‌های مختلف ذخیره می‌شوند

str1 = "hello"
str2 = "hello"
print(str1 is str2)  # True -> رشته‌های کوتاه و بدون فاصله در حافظه مشترک هستند

str3 = "hello world"
str4 = "hello world"
print(str3 is str4)  # احتمالاً False -> چون رشته طولانی‌تر است

```
## Bitwise Operators
### and :  اگر هر دو بیت ۱ باشند، نتیجه ۱ خواهد بود؛ در غیر این‌صورت، ۰ می‌شود.
```python
a = 10    # 1010 در مبنای ۲
b = 4     # 0100 در مبنای ۲
result = a & b
print(result)  # 0 (چون هیچ بیتی در هر دو عدد ۱ نیست)
```
### or : اگر حداقل یکی از بیت‌ها ۱ باشد، نتیجه ۱ خواهد بود.
```python
a = 10    # 1010
b = 4     # 0100
result = a | b
print(result)  # 14 (1110 در مبنای ۲)
```
### xor : اگر دقیقاً یکی از بیت‌ها ۱ باشد، نتیجه ۱ خواهد بود. اگر هر دو بیت ۱ یا هر دو ۰ باشند، نتیجه ۰ می‌شود.
```python
a = 10    # 1010
b = 4     # 0100
result = a ^ b
print(result)  # 14 (1110 در مبنای ۲)
```
### ~ : تمام بیت‌ها را معکوس می‌کند. در پایتون، این اوپراتور در واقع مقدار منفی (n+1) را برمی‌گرداند.
```python
a = 10    # 1010
result = ~a
print(result)  # -11

10 = 0000 1010
11 = 1111 0101

```


# 🎯 20 Combined Operator Examples in Python  
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
