from math import prod, floor as math_floor, ceil as math_ceil

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

def number_to_words(n):
    under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if n < 20:
        return under_20[n]
    elif n < 100:
        return tens[n // 10] + (' ' + under_20[n % 10] if (n % 10 != 0) else '')
    else:
        raise ValueError("This function supports only numbers less than 100")

def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

def is_peterson(n):
    return n == sum(factorial(int(digit)) for digit in str(n))

def is_sunny(n):
    return is_prime(n + 1)

def is_tech_number(n):
    digits = len(str(n))
    if digits % 2 != 0:
        return False
    first_half = n // (10 ** (digits // 2))
    second_half = n % (10 ** (digits // 2))
    return (first_half + second_half) ** 2 == n

def is_fascinating(n):
    concatenated = str(n) + str(n * 2) + str(n * 3)
    return sorted(concatenated) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_keith(n):
    digits = [int(d) for d in str(n)]
    while sum(digits) < n:
        digits.append(sum(digits))
        digits.pop(0)
    return sum(digits) == n

def is_neon(n):
    return sum(int(d) for d in str(n * n)) == n

def is_spy(n):
    digits = [int(d) for d in str(n)]
    return sum(digits) == prod(digits)

def is_autobiographical(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str.count(str(i)) != int(n_str[i]):
            return False
    return True

def is_emirp(n):
    return is_prime(n) and is_prime(int(str(n)[::-1])) and n != int(str(n)[::-1])

def is_sphenic(n):
    prime_factors = [i for i in range(2, n) if n % i == 0 and is_prime(i)]
    return len(prime_factors) == 3

def is_buzz(n):
    return n % 7 == 0 or str(n).endswith('7')

def is_duck(n):
    return '0' in str(n)[1:]

def is_evil(n):
    return bin(n).count('1') % 2 == 0

def is_isbn(n):
    n_str = str(n)
    if len(n_str) == 10:
        return sum((i + 1) * int(d) for i, d in enumerate(n_str)) % 11 == 0
    elif len(n_str) == 13:
        return sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(n_str)) % 10 == 0
    return False

def is_krishnamurthy(n):
    return n == sum(factorial(int(d)) for d in str(n))

def is_bouncy(n):
    increasing, decreasing = False, False
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] < n_str[i + 1]:
            increasing = True
        if n_str[i] > n_str[i + 1]:
            decreasing = True
        if increasing and decreasing:
            return True
    return False

def is_mystery(n):
    for i in range(1, n // 2 + 1):
        if str(i) == str(n - i)[::-1]:
            return True
    return False

def is_smith(n):
    if is_prime(n):
        return False
    sum_digits = sum(int(d) for d in str(n))
    prime_factors_sum = 0
    temp = n
    for i in range(2, n):
        while temp % i == 0:
            prime_factors_sum += sum(int(d) for d in str(i))
            temp //= i
        if temp == 1:
            break
    return sum_digits == prime_factors_sum

def is_strontio(n):
    product = 2 * n
    return 1000 <= product <= 9999 and str(product)[1] == str(product)[2]

def is_xylem(n):
    n_str = str(n)
    mid = len(n_str) // 2
    if len(n_str) % 2 == 0:
        return sum(int(d) for d in n_str[:mid]) == sum(int(d) for d in n_str[mid:])
    else:
        return sum(int(d) for d in n_str[:mid]) == sum(int(d) for d in n_str[mid + 1:])

def nth_prime(n):
    count, num = 0, 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

def alternate_primes(n):
    primes = []
    num, count = 2, 0
    while count < n:
        if is_prime(num):
            if count % 2 == 0:
                primes.append(num)
            count += 1
        num += 1
    return primes

# Arithmetic operations for two or more operands
def add(*args):
    return sum(args)

def subtract(a, b):
    return a - b

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Finding maximum and minimum
def maximum(*args):
    return max(args)

def minimum(*args):
    return min(args)

# Average of numbers
def average(*args):
    return sum(args) / len(args)

# Exponential functions
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def power(base, exp):
    return base ** exp

# Floor and Ceil functions
def floor(n):
    return math_floor(n)

def ceil(n):
    return math_ceil(n)