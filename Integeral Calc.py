def function_to_integrate(x):
    """
    Define the mathematical function you want to integrate here.
    Example: f(x) = x^2
    """
    return x**2


def trapezoidal_integral(f, a, b, n):
    """
    Calculates the definite integral of f(x) from a to b using n panels.
    """

    h = (b - a) / n

    integral = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        integral += f(a + i * h)

    return integral * h


if __name__ == "__main__":
    print("--- Simple Definite Integral Calculator ---")

    lower_limit = 0
    upper_limit = 2
    intervals = 1000

    result = trapezoidal_integral(function_to_integrate, lower_limit, upper_limit, intervals)
    
    print(f"Integrating f(x) = x^2 from {lower_limit} to {upper_limit}")
    print(f"Number of intervals: {intervals}")
    print(f"Calculated Area (Integral): {result:.5f}")