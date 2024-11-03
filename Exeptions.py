try:
    print("Start of Try Block")
    print(15/3)
    print(12/2)
    print(10/0)
    print(value_1)
    print("End of Try Block")

except ZeroDivisionError:
    print("Division by zero")
except NameError:
    print("Такої змінної не існує")

print("Next code")

