name = input("Hello! What's your name? ")
print(f"Nice to meet you, {name}!")
numbers = []
for i in range(1, 4):
    number = int(input(f"Enter your favorite number {i}: "))
    numbers.append(number)
even_odd = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
print("\nLet's check if your numbers are even or odd!")
for num, status in even_odd:
    print(f"The number {num} is {status}.")
print("\nNow, let's explore the square of each number:")
for num in numbers:
    print(f"The square of {num} is {num ** 2}.")
total_sum = sum(numbers)
print(f"\nThe sum of your favorite numbers is {total_sum}. Great choice!")
if total_sum > 1:
    is_prime = True
    for i in range(2, int(total_sum ** 0.5) + 1):
        if total_sum % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"Wow! The sum {total_sum} is a prime number!")
    else:
        print(f"The sum {total_sum} is not a prime number, but it's still awesome!")
else:
    print(f"The sum {total_sum} is not a prime number, but it's still awesome!")