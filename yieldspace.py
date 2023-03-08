""" symbolic math """
from sympy.solvers import solve
from sympy import symbols

c, u, x, y, r, t, T, p = symbols("c,u,x,y,r,t,T,mp")

print("=== Yieldspace v1 ===")
# we have two equations for the price of the bond
# set them equal to each other, solve for x
#   wrong approach is using p = 1-r*t
#      ((2y+x)/x)^-t = 1-r*t
#   correct approach is using p = 1/(1+r*t)
#      ((2y+x)/x)^-t = 1/(1+r*t)
p1_wrong = 1 - r * t  # wrong formula for price
p1 = 1 / (1 + r * t)  # correct formula for price
p2 = ((2 * y + x) / x) ** -t

print(f"calc_bond_reserves (p=1-rt)\n x = {solve(p2 - p1_wrong, x)}")
print(f"calc_bond_reserves (p=1-rt)\n x = {solve(((2 * y + x) / x) ** -t - 1 - r * t, x)}")
print(f"calc_bond_reserves (p=1/(1+rt))\n x = {solve(p2 - p1, x)}")
print(f"solve for p in yieldspace:\n p = {solve(r - (1 / p) ** (1 / t) - 1, p)}")

print("=== Yieldspace v2 ===")
# we have two equations for the price of the bond
# set them equal to each other, solve for x
#   wrong approach is using p = 1-r*t
#      ((c * (2 * y + x)) / (u * x)) ** -T = 1-r*t
#   correct approach is using p = 1/(1+r*t)
#      ((c * (2 * y + x)) / (u * x)) ** -T = 1/(1+r*t)
p3_wrong = 1 - r * t
p3 = 1 / (1 + r * t)
p4 = ((c * (2 * y + x)) / (u * x)) ** -T

sol4 = solve(p4 - p3_wrong, x)
print(f"x_reserves (p=1-rt)\n x = {sol4}")
sol4 = solve(p4 - p3, x)
print(f"x_reserves (p=1/(1+rt))\n x = {sol4}")
