# Problem of the day 2:
# user should enter array of number and you are giving the number
# one of the two numbers that equals the sum of the given number

numbers = list(map(int, input("Enter the array numbers by spaces: ").split()))
target_sum = int(input("Enter the target sum: "))

for num in numbers:
    if target_sum - num in numbers:
        print(f"Pair found: ({num}, {target_sum - num})")