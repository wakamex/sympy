""" symbolic math """

import sympy as sym
from sympy import symbols

# declare all variables in one line
c, u, x, y, r, t, T, p, z, delta_z, delta_y, d, mu, tau, k, J = symbols(
    "c,u,x,y,r,t,T,mp,z,delta_z,delta_y,d,mu,tau,k,J"
)

print("Systems of linear equations")
# Sympy is able to solve a large part of polynomial equations, and is also capable of solving multiple equations with
# respect to multiple variables giving a tuple as second argument. To do this you use the solve() command:
# https://scipy-lectures.org/packages/sympy.html
solution = sym.solve(
    (x + 5 * y - 2, -3 * x + 6 * y - 15),
    (x, y),
)
print(f"{solution[x]=}, {solution[y]=}")

print("yieldspace system of equations, solve for delta_y")
# originally this described the stock of z and y, we added delta_z (pool reserves)
# z - dz = (y + dy) / (mu * (1 - rt)**(1/tau))
# mu * ( 1 - rt)**(1/tau) = J

# with deltas
print("equation 1: z - delta_z = (y + delta_y) / (mu * (1 - rt)**(1/tau))")
equation_1 = sym.Eq(z - delta_z, (y + delta_y) / (mu * (1 - r * t) ** (1 / tau)))
# without deltas
# print("equation 1: z = (y) / (mu * (1 - rt)**(1/tau))")
# equation_1 = sym.Eq(z, (y) / (mu * (1 - r * t) ** (1 / tau)))
# calc in give out (swap transaction)
print("equation 2: delta_y = (k - (c / mu) * (mu * (z - delta_z))**(1 - tau))**(1 / (1 - tau)) - (2y + cz)")
equation_2 = sym.Eq(delta_y, (k - (c / mu) * (mu * (z - delta_z)) ** (1 - tau)) ** (1 / (1 - tau)) - (2 * y + c * z))
equation_3 = sym.Eq(
    delta_z, (1 / mu) * ((k - (2 * y + c * z - delta_y) ** (1 - tau)) / (c / mu)) ** (1 / (1 - tau)) - z
)
# solve with EQ1 and EQ2
# solution = sym.solve((equation_1, equation_2), (delta_y))
# print(f"{solution[delta_y]=}")

# we have EQ1 and EQ1
# rearrange EQ1 isolating delta_z on the left hand side
print(f"EQ1: {sym.solve(equation_1, delta_y)=}")
# rearrange EQ2 isolating delta_z on the left hand side
print(f"EQ2: {sym.solve(equation_2, delta_y)=}")
# solution is delta_y = [-c*z - 2*y + (c*(delta_z*mu - mu*z)/(mu*(-delta_z*mu + mu*z)**tau) + k)**(-1/(tau - 1))]
# rearrange EQ3 isolating delta_z on the left hand side
print(f"EQ3: {sym.solve(equation_3, delta_y)=}")
# gives same result
# solution is delta_y = [-c*z - 2*y + (c*(delta_z*mu - mu*z)/(mu*(-delta_z*mu + mu*z)**tau) + k)**(-1/(tau - 1))]
# set the right hand sides equal to each other

delta_z_rhs_1 = sym.solve(equation_1, delta_z)[0]
print(f"{delta_z_rhs_1=}")
delta_z_rhs_2 = sym.solve(equation_3, delta_z)[0]
print(f"{delta_z_rhs_2=}")
new_equation = sym.Eq(delta_z_rhs_1, delta_z_rhs_2)
print(f"{new_equation=}")
print("solve for delta_y")
solution = sym.solve(new_equation, delta_y)
print(f"{solution=}")
