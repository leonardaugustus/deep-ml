import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g_coeffs(x)/h_coeffs(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    def calc_f(f_coeffs,x):
        r = 0
        n = len(f_coeffs)
        for i in range(n):
            r += f_coeffs[i] * x ** (n - i - 1)
        return r

    def calc_der(f,x):
        r = 0
        n = len(f)
        for i in range(n):
            r += (n - i - 1) * f[i] * x ** (n - i - 1 - 1)
        return r
    try:
        return (calc_der(g_coeffs, x) * calc_f(h_coeffs, x) - calc_f(g_coeffs,x) * calc_der(h_coeffs, x)) / (calc_f(h_coeffs, x)**2)
    except ZeroDivisionError:
        return -1


 