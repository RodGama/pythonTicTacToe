prime_numbers = list()
for num in range(2, 1000 + 1):
    if all(num % i != 0 for i in range(2, num)):
        prime_numbers.append(num)
