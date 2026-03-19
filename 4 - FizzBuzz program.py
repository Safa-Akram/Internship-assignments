def fizzbuzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif num % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif num % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(num)

    return fizz_count, buzz_count, fizzbuzz_count


# Function Call
fizz, buzz, fizzbuzz_total = fizzbuzz()

print("\n--- Total Occurrences ---")
print("Total Fizz:", fizz)
print("Total Buzz:", buzz)
print("Total FizzBuzz:", fizzbuzz_total)