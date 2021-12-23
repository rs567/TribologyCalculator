from math import gamma
from sympy import solve
from sympy import expand
import sympy as sp
from sympy.core.symbol import symbols
alpha, mu, gamma, l, rho, pi, f = sp.symbols(alpha, mu, gamma, l, rho, pi, f )
SolutionForPi = sp.Eq((alpha*mu*(-gamma*l*rho + gamma*l - gamma*pi*rho + gamma*pi - l*rho - pi*rho)/(-rho/(rho - 1) + 1) + pi*mu)-pi)
SolutionForPi = solve(SolutionForPi, pi)

ExpandSolution = expand(SolutionForPi[0])
[mu*(-alpha*gamma*l*rho**2 + 2*alpha*gamma*l*rho - alpha*gamma*l - alpha*l*rho**2 + alpha*l*rho - f)/(alpha*gamma*mu*rho**2 - 2*alpha*gamma*mu*rho + alpha*gamma*mu + alpha*mu*rho**2 - alpha*mu*rho - 1)]