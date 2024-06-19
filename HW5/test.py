import numpy as np

def numerical_gradient(f, p, h=1e-5):
    grad = np.zeros_like(p)
    for i in range(len(p)):
        p_plus_h = np.copy(p)
        p_plus_h[i] += h
        f_plus_h = f(p_plus_h)

        p_minus_h = np.copy(p)
        p_minus_h[i] -= h
        f_minus_h = f(p_minus_h)

        grad[i] = (f_plus_h - f_minus_h) / (2 * h)
    return grad

def gradientDescendent(f, p, learning_rate=0.01, iterations=100):
    for i in range(iterations):
        grad = numerical_gradient(f, p)
        p -= learning_rate * grad
        print(f"Iteration {i+1}: p = {p}, f(p) = {f(p)}")

# 測試函數
def f(p):
    [x, y, z] = p
    return (x-1)**2 + (y-2)**2 + (z-3)**2

# 初始參數
p = np.array([0.0, 0.0, 0.0])

# 執行梯度下降法
gradientDescendent(f, p)


