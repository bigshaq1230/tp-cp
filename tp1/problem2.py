def f(ch: str):
    input_numbers = list(map(int, ch.split()))  # O(n) Convert input string to a list of integers

    l = input_numbers[:3]  # O(1) Get a list of the kids' candy
    n = input_numbers[3]   # O(1) Get the number of candies from dad

    moy = sum(l) % 3  # O(1) Calculate the sum of the candies and mod by 3

    if moy == 0 and min(l) > n // 3:  # O(1) Check if sum is divisible by 3 and smallest number is greater than n/3
        print("YES")  # O(1) Print "YES" if conditions are met
    else:
        print("NO")   # O(1) Otherwise, print "NO"

x = int(input())  # O(1) Number of test cases
for i in range(x):
    f(input())  # O(n) Run the function for each test case (input string processing takes O(n))
