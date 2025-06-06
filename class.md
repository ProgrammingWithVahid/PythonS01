```python
class Car:
    def __init__(self, color, name, speed):
        self.color = color
        self.name = name
        self.speed = speed

    def double_speed(self):
        self.speed *= 2

    def show_detail(self):
        print("car color: ",self.color, ",car name: " ,self.name)

bmw = Car("red", "bmw", 200)
bmw.show_detail()
print(bmw.double_speed())

mercedes = Car("khaki", "mercedes", 250)
mercedes.show_detail()
print(mercedes.double_speed())
```
```python
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

p1 = Person("Ali", 30)
p1.introduce()
```
### class methods  cls
```python
class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def show_total(cls):
        print(cls.total_cars)

Car()
Car()
Car.show_total()  # output: 2
```

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    
    def how_many(self):
        print(f"There are {self.count} students.")

Student("Sara")
Student("Reza")
Student.how_many()
```

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def how_many(cls):
        print(f"There are {cls.count} students.")

Student("Sara")
Student("Reza")
Student.how_many()

```
### Dunder Methods -- Double UNDERscore 
### __init__   initializer 

### _ underscore _name  -> private
### __ underscore  __name   -> name mangling
```python
class Test:
    def __init__(self):
        self.__secret = "hidden"

t = Test()
# print(t.__secret)  ← false
print(t._Test__secret)  # this is correct
```
