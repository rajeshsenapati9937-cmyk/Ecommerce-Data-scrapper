# Generate all even numbers less than 100

# Method 1: Using a list comprehension
even_numbers = [num for num in range(2, 100, 2)]
print("Even numbers less than 100:")
print(even_numbers)

# Method 2: Using a loop
print("\nEven numbers using a loop:")
for num in range(2, 100, 2):
    print(num, end=" ")
print()

# Method 3: Count of even numbers
print(f"\nTotal count of even numbers less than 100: {len(even_numbers)}")
