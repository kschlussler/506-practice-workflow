import pandas as pd
import numpy as np

number_var = 42
string_var = "Hello, Friends!"
list_var = [1, 2, 3, 4, 5]
dict_var = {
    "name": "Kate",
    "age": 32,
    "attributes": {
        "height": "5'6",
        "hobbies": ["Coding", "Shopping", "Reading"]
    },
    "is_student": True
}

def analyze_number(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    else:
        return f"{num1} is not greater than {num2}"

result = analyze_number(10, 20)
print("Comparison Result:", result)

def analyze_number(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    else:
        return f"{num1} is not greater than {num2}"

result = analyze_number(10, 20)

print("Comparison Result:", result)
print("Number:", number_var)
print("String:", string_var)
print("List:", list_var)
print("Dictionary:", dict_var)
