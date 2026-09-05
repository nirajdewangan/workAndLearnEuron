# ============================================================
# 9. PRIME NUMBER ANALYZER
# ============================================================

def is_prime(number):
    """Return True if number is prime."""
    if number <= 1:
        return False

    divisor = 2

    while divisor * divisor <= number:

        if number % divisor == 0:
            return False

        divisor += 1

    return True


def find_primes(start, end):
    """Return prime numbers within a range."""
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


def prime_total(primes):
    """Return total of prime numbers."""
    total = 0

    for number in primes:
        total += number

    return total


def largest_prime(primes):
    """Return largest prime without max()."""
    if len(primes) == 0:
        return None

    largest = primes[0]

    for number in primes:
        if number > largest:
            largest = number

    return largest


def prime_number_analyzer():
    """Run Prime Number Analyzer."""
    start = int(input("Enter range start: "))
    end = int(input("Enter range end: "))

    primes = find_primes(start, end)

    print("Prime Numbers:", primes)
    print("Prime Count:", len(primes))
    print("Prime Sum:", prime_total(primes))
    print("Largest Prime:", largest_prime(primes))


prime_number_analyzer()