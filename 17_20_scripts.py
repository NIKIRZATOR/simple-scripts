import random
import math


def km_info_mile():
    km = random.randint(1, 50)
    miles = km * 0.621
    print(f"{km} km is {miles} miles")

def min_value_of_3():
    print("\n")
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    c= random.randint(1, 50)
    min_value = min(a, b, c)
    print(f"Minimal value from {a}, {b}, {c} is {min_value}")

def print_string():
    print("\n")
    name = "Hello world"
    print(name)

def factorial_value():
    print("\n")
    a = random.randint(1, 5)
    b = math.factorial(a)
    print(f"Factorial {a} is {b}")

def input_format():
    print("\n")
    input_int = 123
    input_float = 5.54
    input_string = "aboba"

    print(f"{input_int} in format{type(input_int)}\n"
          f"{input_float} in format {type(input_float)}\n"
          f"{input_string} in format {type(input_string)}")

def simple_values():
    print("\n")
    a = random.randint(3, 51)
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if(k <= 0):
        print(f"{a} is simple value")
    else:
        print(f"{a} is composite value")

def multiplication_table():
    print("\n")
    a = random.randint(1, 10)
    for i in range(1, 11):
        print(f"{a} * {i} = {a * i}")

def visokosnii_or_not_year():
    print("\n")
    year = random.randint(1500, 3000)
    if year % 4 == 0:
        print(f"Year {year} is visokosnii year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is visokosnii")
        else:
            print(f"Year {year} is`n visokosnii")
    else:
        print(f"Year {year} is`n visokosnii")

def find_person_ASCII():
    print("\n")
    pass

def simvol_into_ASCII():
    print("\n")
    a = 88
    b = "XYZ"
    c = chr(a)
    print(f"Length {b} is {len(b)}")
    print(f"Code of {a} is {c}")
    print(f"{[ord(i) for i in b]}")

def HCF():
    print("\n")
    a = random.randint(10, 50)
    a_arr = []
    b = random.randint(10, 50)
    b_arr = []

    i = 1
    for i in range(i, a):
        if a % i == 0:
            a_arr.append(i)
        i = i+1

    j = 1
    for j in range(j, b):
        if b % j == 0:
            b_arr.append(j)
        j = j + 1

    c_arr = []
    for p in a_arr:
        for l in b_arr:
            if p == l:
                c_arr.append(p)
    #print(c_arr)
    print(f"HCF of {a} and {b} is {max(c_arr)}")

def lambda_func():
    print("\n")
    a = random.randint(1, 10)
    func_1 = a * a * a
    func_2 = lambda a: a * a * a

    print(f"Result of func_1 and func_2 is the same: {a}^3 = {func_2(a)} and {func_1}")

def add_2_float():
    print("\n")
    a = 4.78
    b = 1.49

    sum = float(a) + float(b)
    print(f"Sum of {a} + {b} = {sum}")

def even_or_not_value():
    print("\n")
    a = random.randint(1, 50)

    if a % 2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is`n even")

def count_glasnii_and_soglasnii():
    print("\n")
    letters = "qwertyuiopasdfghjklzxcvbnm"
    glas = 'aeiouy'

    stroka = ""
    for i in range(1, 11):
        stroka += random.choice(letters)
    g = 0
    s = 0
    for j in stroka:
        if j not in glas:
            s += 1
        else:
            g += 1
    print(f"Word if {stroka}")
    print(f"Glasnii = {g}, soglasnii = {s}")

def positive_negative_zero():
    print("\n")
    a = random.randint(-100, 100)

    if a < 0:
        print(f"{a} is negative number")
    elif a == 0:
        print(f"{a} is zero")
    else:
        print(f"{a} is positive number")

def simple_calc():
    print("\n")
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

def main():
    km_info_mile()
    min_value_of_3()
    print_string()
    factorial_value()
    input_format()
    simple_values()
    multiplication_table()
    visokosnii_or_not_year()
    find_person_ASCII()
    simvol_into_ASCII()
    HCF()
    lambda_func()
    add_2_float()
    even_or_not_value()
    count_glasnii_and_soglasnii()
    positive_negative_zero()
    simple_calc()

if __name__ == main():
    main()
