def primeChecker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("It is a prime number")
    else:
        print("Not a prime number")

n = int(input("Check this number: "))
primeChecker(n)