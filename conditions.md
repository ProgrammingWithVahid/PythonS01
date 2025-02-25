# Conditions 

## 1. if
```python
age = 20
if age >= 18:
    print("شما مجاز به رانندگی هستید.")
```

## 2. if - else (اگر - در غیر این صورت)
```python
age = 16
if age >= 18:
    print("شما مجاز به رانندگی هستید.")
else:
    print("شما هنوز مجاز به رانندگی نیستید.")
```
###  شرط‌های تو در تو (Nested Conditions)
```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("شما مجاز به رانندگی هستید.")
    else:
        print("لطفاً گواهینامه بگیرید.")
else:
    print("سن شما کافی نیست.")
```
### استفاده از شرط در یک خط (تعبیر شرطی یا Ternary Operator)
```python
age = 20
message = "Ok!" if age >= 18 else "Not Ok!"
print(message)
```
```python
num = 7
parity = "Even" if num % 2 == 0 else "Odd"

print(parity)  # خروجی: "Odd"
```
```python
a, b = 5, 10
bigger = a if a > b else b

print(bigger)  # خروجی: 10
```
## 3. if - elif - else (اگر - در غیر این صورت اگر - در غیر این صورت)
```python
score = 85

if score >= 90:
    print("نمره شما عالی است.")
elif score >= 75:
    print("نمره شما خوب است.")
else:
    print("نیاز به تلاش بیشتر دارید.")
```
### استفاده از match-case در پایتون 3.10+
از match برای جایگزینی if-elif-else در برخی شرایط استفاده می‌شود.
```python
day = "Sat"

match day:
    case "Mon":
        print("Start of the week!")
    case "Sun" | "Sat":
        print("Off day!")
    case _:
        print("Normal day")
```


### Comparison Operators(اوپراتورهای مقایسه‌ای) == != < > =< =>
### Logical Operators(اوپراتورهای منطقی) and or not
### link to Operators in youtube: https://youtu.be/6GphqYhGWKg?si=jzc1pY60DiKW3lkP
### github link: https://github.com/ProgrammingWithVahid/PythonS01/blob/main/combined_operator_examples.md
```python
x = 7
y = 15

if x > 5 and y > 10:
    print("هر دو شرط برقرار است.")
```

## Points

### in
```python
vowels = "aeiou"
letter = "e"

if letter in vowels:
    print("حرف صدادار است.")
```
### Checking Length
```python
names = []

if not names:
    print("لیست خالی است.")
```

### مقداردهی شرطی با or و and
#### Or
```python
name = input("your name: ") or "undefined!"
print(f"سلام، {name}!")
```
#### And
```python
x = 10
y = 5
result = x > y and "x Greater" or "y greater"
print(result)
```
### all()
اگر همه مقادیر در یک لیست یا مجموعه True باشند، مقدار True برمی‌گرداند:
```python
conditions = [True, True, False]
if all(conditions):
    print("همه‌ی شرط‌ها برقرارند.")
else:
    print("حداقل یکی از شرط‌ها برقرار نیست.")
```
### any()
حداقل یکی از موارد درست باشد
```python
conditions = [False, False, True]

if any(conditions):
    print("حداقل یکی از شرط‌ها برقرار است.")
```
### else if - elif
❌
```python
score = 85

if score >= 90:
    print("نمره عالی")
else:
    if score >= 75:
        print("نمره خوب")
    else:
        print("نیاز به تلاش بیشتر")
```
✅ elif
```python
score = 85

if score >= 90:
    print("نمره عالی")
elif score >= 75:
    print("نمره خوب")
else:
    print("نیاز به تلاش بیشتر")
``` 
✅ کد خواناتر و کوتاه‌تر شده است.
### match-case is better than if-elif-else
```python
match day:
    case "Mon":
        print("Start of the week!")
    case "Sun" | "Sat":
        print("Off day!")
    case _:
        print("Normal day")
```

## شرط پیچیده با all() و any() برای اعتبارسنجی رمز عبور
```python
password = "Python123!"

conditions = [
    any(c.isdigit() for c in password),  # حداقل یک عدد داشته باشد
    any(c.islower() for c in password),  # حداقل یک حرف کوچک داشته باشد
    any(c.isupper() for c in password),  # حداقل یک حرف بزرگ داشته باشد
    any(c in "!@#$%^&*()" for c in password),  # حداقل یک کاراکتر خاص داشته باشد
    len(password) >= 8  # حداقل طول ۸ باشد
]

if all(conditions):
    print("رمز عبور قوی است.")
else:
    print("رمز عبور ضعیف است.")

```
 c همین‌جا داخل for c in password تعریف می‌شه!
 به این نوع تعریف متغیر، "تعریف درون حلقه (for-loop variable)" می‌گن.

 ## چک کردن اشتراک لیست‌ها بدون حلقه
 ```python
list1 = [1, 2, 3, 4, 5]
list2 = [10, 9, 8, 3]

if set(list1) & set(list2):
    print("دو لیست مقدار مشترک دارند.")
else:
    print("اشتراکی وجود ندارد.")

# & : Intersection اشتراک
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 & set2)  # {3}
```
## شرط‌های تو در تو برای اولویت‌بندی تخفیف فروشگاه
 ```python
amount = 500  # مبلغ خرید
membership = "gold"  # نوع عضویت

if amount > 300:
    if membership == "gold":
        discount = 30
    elif membership == "silver":
        discount = 20
    else:
        discount = 10
else:
    discount = 5

print(f"میزان تخفیف: {discount}%")
 ```

## کد پیچیده برای تشخیص سال کبیسه
 ```python
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("سال کبیسه است.")
else:
    print("سال کبیسه نیست.")
 ```
