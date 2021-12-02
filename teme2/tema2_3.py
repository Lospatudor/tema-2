def my_function():
    try:
        number = int(input("Insert Number: "))
        print(f"This is Your number: {number}")
    except ValueError:
        print("0")


my_function()