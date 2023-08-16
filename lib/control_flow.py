#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin" and password == "12345":
        return "Access granted"
    elif username == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))
print(admin_login("sudo", "12345"))


def hows_the_weather(temperature):
    if temperature <= 39:
        return "It's brisk out there!"
    elif temperature <= 64:
        return "It's a little chilly out there!"
    elif temperature <= 65 or temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

print(hows_the_weather(33))
print(hows_the_weather(99))
print(hows_the_weather(75))


def fizzbuzz(num):
    result1 = num % 3
    result2 = num % 5

    if result1 == 0 and result2 == 0:
        return "FizzBuzz"
    elif result1 == 0:
        return "Fizz"
    elif result2 == 0:
        return "Buzz"
    else:
        return num

print(fizzbuzz(1))
print(fizzbuzz(2))
print(fizzbuzz(3))
print(fizzbuzz(4))
print(fizzbuzz(5))
print(fizzbuzz(15))

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        print("Invalid operation!")
        return None

print(calculator("+", 1, 1))
print(calculator("-", 3, 1))
print(calculator("*", 3, 2))
print(calculator("/", 4, 2))
print(calculator("nope", 4, 2))
