# Debug Celsius Converter (8 kyu)

- **Language:** Python  
- **Kata Link:** https://www.codewars.com/kata/55cb854deb36f11f130000e1/solutions/python
- **Description:**  
  The task was to debug a program that converts Fahrenheit to Celsius.  
  The original code had syntax and logic issues.  
  The correct formula is:  
  `celsius = (fahrenheit - 32) * (5/9)`

- **Fix Summary:**  
  1. Replaced `:` with `=` when assigning a variable.  
  2. Corrected the function call and variable names.  
  3. Used `if c <= 0` to check freezing temperature.  
  4. Returned a formatted string with the Celsius value.

- **Notes:**  
  Make sure to test both positive and negative Fahrenheit values.