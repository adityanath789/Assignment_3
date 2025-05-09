import math
try:
  number = float(input("Enter a number: "))
  sqrt_result = math.sqrt(number)
  log_result = math.log(number)
  sin_result = math.sin(number)
  print("Square root:", sqrt_result)
  print("Logarithm:", log_result)
  print("Sine:", sin_result)
except ValueError:
  print(f"Square root of {number} is {sqrt_result}")
  print(f"Natural logarithm of {number} is {log_result}")
  print(f"Sine of {number} radians is {sin_result}")

except ValueError as e:
  print(f"Error: {e}.Please enter a valid positive number.")
