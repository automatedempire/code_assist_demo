def calculate_factorial_buggy(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
