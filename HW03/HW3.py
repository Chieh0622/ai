# 參考https://github.com/LeeYi-user/ai/blob/master/homework/03/linear.py
from scipy.optimize import linprog

c = [-3, -2, -5]

A = [
    [1, 1, 0],   # x + y <= 10
    [2, 0, 1],   # 2x + z <= 9
    [0, 1, 2]    # y + 2z <= 11
]

b = [10, 9, 11]

x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

if result.success:
    print('Optimal value:', -result.fun)
    print('x:', result.x[0])
    print('y:', result.x[1])
    print('z:', result.x[2])
else:
    print('No solution found')
