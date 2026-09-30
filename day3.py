import math
age = 32
height = 6.9
complex_num = 1 + 5j
base = 20
triangle_height = 10
area_triangle = 0.5 * base * triangle_height
print(f"The area of the triangle is {area_triangle}")
side_a = 5
side_b = 4
side_c = 3
perimeter_triangle = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter_triangle}")
length = 10
width = 5
area_rect = length * width
perimeter_rect = 2 * (length + width)
print(f"Area: {area_rect}, Perimeter: {perimeter_rect}")
radius = 10
pi = 3.14
area_circle = pi * (radius**2)
circumference = 2 * pi * radius
print(f"Area: {area_circle}, Circumference: {circumference}")
slope_1 = 2
y_intercept = -2
x_intercept = 1  
print(
    f"Slope: {slope_1}, Y-intercept: (0, {y_intercept}), X-intercept: ({x_intercept}, 0)"
)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
euclidean_dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Slope: {slope_2}, Euclidean distance: {euclidean_dist}")
print("Slopes are equal:", slope_1 == slope_2)
x = -3
y = x**2 + 6 * x + 9
print(f"Value of y when x is {x}: {y}")
print(len("python") != len("dragon"))
print("on" in "python" and "on" in "dragon")
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)
print(not ("on" in "dragon" and "on" in "python"))
len_python = len("python")
float_len = float(len_python)
str_len = str(float_len)
print(str_len, type(str_len))
number = 10
is_even = number % 2 == 0
print(f"Is {number} even?", is_even)
print(7 // 3 == int(2.7))
print(type("10") == type(10))
try:
    print(int("9.8") == 10)
except ValueError:
    print("int('9.8') throws ValueError; int(float('9.8')) == 10 is", int(float("9.8")) == 10)
hours = 40
rate = 28
weekly_earning = hours * rate
print(f"Your weekly earning is {weekly_earning}")
years = 100
seconds_lived = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds.")
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")