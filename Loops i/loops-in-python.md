# Loops in Python

## 1. حلقه for (برای تکرار روی مجموعه‌ای از عناصر)
## 2. حلقه while (برای تکرار تا زمانی که یک شرط برقرار است)
## for
```python
for متغیر_حلقه in دنباله:
    # ...
```
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```
```python
text = "Python"
for char in text:
    print(char)
```
`range(start, stop, step)`
`range(5)` -> `0 1 2 3 4`
`range(1, 10, 2)` -> `1 3 5 7 9`
```python
for i in range(5):  # مقدارهای 0 تا 4
    print(i)
```

## while
```python
while شرط:
    # ...
```
```python
count = 0
while count < 5:
    print(count)
    count += 1  # افزایش مقدار شمارنده


while True:
    command = input("Enter 'stop' to exit: ")
    if command == 'stop':
        break
```

## دستورات کنترلی در حلقه‌ها
### break
```python
for i in range(10):
    if i == 5:
        break  # خروج از حلقه
    print(i)
```
### continue 
```python
for i in range(5):
    if i == 2:
        continue  # از این مقدار عبور می‌کند
    print(i)
```
### else
```python
for i in range(5):
    print(i)
else:
    print("حلقه به پایان رسید.")
```
## Nested Loops
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```
## Tippes
### dict
```python
data = {"name": "Ali", "age": 25, "city": "Tehran"}
for key in data:
    print(key)  # فقط کلیدها را چاپ می‌کند

for key, value in data.items():
    print(f"{key}: {value}")
```
### List Comprehension
```python
numbers = []
for i in range(5):
    numbers.append(i * 2)

numbers = [i * 2 for i in range(5)]
```
### while True
```python
while True:
    text = input("type 'exit' to exit: ")
    if text == "exit":
        break
```
### zip()
```python
names = ["Ali", "Ali 1", "Ali 2"]
ages = [71, 73, 62]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```
### reversed()
```python
for i in reversed(range(5)):
    print(i)
```
### pass
اگر نیاز دارید حلقه‌ای بنویسید که بعداً آن را تکمیل کنید، می‌توانید از `pass` استفاده کنید تا خطا نگیرید.
```python
for i in range(5):
    pass  # بعداً اینجا کد اضافه می‌کنیم
```
