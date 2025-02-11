# لیست ساده از اعداد (Integer List)
numbers = [100, 205, 323, 443, 597]
#index : 0 1 2 3 4
print(numbers[2])
print(numbers)

# فراموش کردن کروشه [] در تعریف لیست
my_list = 1, 2, 3
print(type(my_list)) # this is Tuple

# لیست شامل انواع داده مختلف (Mixed Data Types)
mixed_list = [10, "Python", 3.14, True, None]
print(mixed_list)

#لیست تو در تو (Nested List)
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested_list)

#لیست خالی (Empty List)
empty_list = []
print(empty_list)

# پروژه: سیستم مدیریت دانشجویان
# این برنامه اطلاعات دانشجویان رو ذخیره، فیلتر و پردازش می‌کنه.

# مقداردهی اولیه لیست با مقدار خاص / پر کردن لیست با مقدار پیش‌فرض
default_grades = [10] * 50  # فرض کن دانشجو هنوز نمره‌ نداره
print("نمرات پیش‌فرض برای دانشجو جدید:", default_grades)

# تعریف لیست اطلاعات دانشجویان
students = [
    {"id": 101, "name": "Ali", "age": 22, "grades": [18, 17, 19]},
    {"id": 102, "name": "Sara", "age": 20, "grades": [15, 16, 14]},
    {"id": 103, "name": "Reza", "age": 23, "grades": [10, 12, 11]},
    {"id": 104, "name": "Mina", "age": 21, "grades": [19, 20, 18]},
    {"id": 105, "name": "Hassan", "age": 24, "grades": [8, 9, 7]}
]
#   [start:end:step]    برش (Slicing)
# نمایش آخرین دانشجو
print("آخرین دانشجو اضافه شده:", students[-1])

# نمایش سه دانشجوی آخر لیست
print("سه دانشجوی آخر لیست:", students[-3:])

# برعکس کردن لیست دانشجویان
print("لیست معکوس دانشجویان:", students[::-1])

#  ترکیب نمرات همه دانشجویان به یک لیست مسطح
# Loop
# داخل پرانتز حلقه ها در پایتون
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for student in students:
    for grade in student["grades"]:
        all_grades0.append(grade)
        # انجام کارهایی با grade
all_grades = [grade for student in students for grade in student["grades"]]
print("لیست همه نمرات:", all_grades)

#  حذف مقادیر تکراری از لیست
unique_grades = list(set(all_grades))
print("نمرات بدون تکرار:", unique_grades)

# تبدیل لیست به انواع دیگر دیتا تایپ
#names = []
#for student in students:
#    names.append(student["name"])
#result = tuple(names)
names_tuple = tuple(student["name"] for student in students)
names_set = set(student["name"] for student in students)
print("لیست به تاپل:", names_tuple)
print("لیست به ست:", names_set)

# Tip
#  بررسی عدم امکان تبدیل عدد به لیست
try:
    num_to_list = list(123)
except TypeError:
    print("خطا: عدد را نمی‌توان به لیست تبدیل کرد زیرا عدد یک مقدار iterable نیست.")

#  مقدار دهی چندگانه به اطلاعات یک دانشجو
student_id, student_name, student_age = [106, "Ehsan", 25]
print(f"دانشجوی جدید: ID={student_id}, نام={student_name}, سن={student_age}")

# کپی کردن لیست دانشجویان به روش‌های مختلف
students_copy = students[:]
students_deep_copy = [student.copy() for student in students]
print("کپی سطحی لیست:", students_copy)
print("کپی عمیق لیست:", students_deep_copy)

# ایجاد ارجاع، نه کپی واقعی
list1 = [1, 2, 3]
list2 = list1  # حالا هر تغییری در list2 روی list1 هم اعمال می‌شود!
list2[0] = 100
print(list1)  # خروجی: [3, 2, 100] ❌

list1 = [1, 2, 3]
list2 = list1.copy()  # یا list1[:]
list2[0] = 100
print(list1)  # خروجی: [3, 2, 1] ✅


#  لیست چند بعدی (نمایش نمرات دانشجویان به شکل جدول)
grades_matrix = [student["grades"] for student in students]
print("ماتریس نمرات دانشجویان:", grades_matrix)
print("دسترسی به نمره دوم دانشجوی دوم:", grades_matrix[1][1])

# گرفتن تمام نمرات یک دانشجو خاص (مثلاً دانشجوی سوم)
student_3_grades = students[2]["grades"]
print("نمرات دانشجوی سوم:", student_3_grades)





#  حذف مقدار خاص از لیست بدون استفاده از حلقه for
all_grades_without_10 = [x for x in all_grades if x != 10]
print("لیست نمرات بدون مقدار 10:", all_grades_without_10)

# حذف تمام مقدارهای None یا 0 از لیست نمرات
mixed_data = [18, None, 15, 0, 12, None, 20, 0]
cleaned_data = [x for x in mixed_data if x not in [None, 0]]
print("لیست نمرات پس از حذف None و 0:", cleaned_data)

# فیلتر کردن دانشجویانی که میانگین نمراتشان بالای 15 است
high_achievers = [student for student in students if sum(student["grades"]) / len(student["grades"]) > 15]
print("دانشجویان با میانگین نمره بالای 15:", high_achievers)

#  جستجو در لیست: پیدا کردن دانشجویی با ID خاص
result_student = [student for student in students if student["id"] == 103]

print("جستجوی دانشجو با ID 103:", result_student)

# تکنیک‌های پیشرفته Slicing
print("هر دو مقدار در میان:", all_grades[::2])
print("برش لیست از ایندکس 2 تا 5:", all_grades[2:6])
