
try:
    num = input("Enter a number: ")  # Take user input
    num = int(num)  # Convert input to integer
    for i in range(1, 11):
        print(num * i)  # Multiply the input number by i and print the result
except Exception as e:
    print(f"Error: {e}")  # Print the error message

finally:
    print("Some lines of code")  # Additional handling in case of error
print("End of the program")  # This will always execute

