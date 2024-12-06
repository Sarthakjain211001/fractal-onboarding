try:
    age = int(input("Enter age:"))
    assert age>0, "Age must be greater than 0."
except AssertionError as e:
    print(f"Error: {e}")
except ValueError:
    print("Enter a valid numnber")
else:
    print(f"Your age: {age}")