## Game in python

### Detailed Description

1. **User Input - Name**:

   - The program starts by asking for the user's name and greets them using their input.

   ```python
   name = input("Hello! What's your name? ")
   print(f"Nice to meet you, {name}!")
   ```

2. **User Input - Favorite Numbers**:

   - An empty list `numbers` is created. Then, a loop collects three numbers from the user and appends them to the list.

   ```python
   numbers = []
   for i in range(1, 4):
       number = int(input(f"Enter your favorite number {i}: "))
       numbers.append(number)
   ```

3. **Even or Odd Check**:

   - The list comprehension checks if each number in `numbers` is even or odd and stores the result in `even_odd`.

   ```python
   even_odd = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
   ```

4. **Output - Even/Odd Results**:

   - The program iterates through `even_odd` to print whether each number is even or odd.

   ```python
   print("\nLet's check if your numbers are even or odd!")
   for num, status in even_odd:
       print(f"The number {num} is {status}.")
   ```

5. **Output - Squares of Numbers**:

   - The program calculates and prints the square of each number in the list.

   ```python
   print("\nNow, let's explore the square of each number:")
   for num in numbers:
       print(f"The square of {num} is {num ** 2}.")
   ```

6. **Sum Calculation**:

   - The sum of the user's numbers is calculated and displayed.

   ```python
   total_sum = sum(numbers)
   print(f"\nThe sum of your favorite numbers is {total_sum}. Great choice!")
   ```

7. **Prime Check**:
   - The program checks if the sum is prime by testing divisibility. It prints whether the sum is prime or not.
   ```python
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
   ```

---
