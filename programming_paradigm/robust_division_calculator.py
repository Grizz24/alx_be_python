def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        result = num1 / num2
        print(f"The result of the division is {result}")
    except ValueError:
        return "Error: Please enter valid numeric values only."
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


