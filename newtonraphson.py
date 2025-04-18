# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 13:32:38 2025

@author: pc
"""
#newton-raphson
import sympy as sp

# Sembolik değişken
x = sp.Symbol('x x1 x3')

# Fonksiyon tanımı
f=(x1 - 2*x2 + x3 + 1)**2 + (x1 + x2 - x3 + 3)**2 + (-2*x1 + x2 - x3)**2
# Türevler (otomatik)
f1 = sp.diff(f, x1)
f2 = sp.diff(f1, x2)
f3 = sp.diff(f2,x3)
# Sayısal hale getir
f_ = sp.lambdify(x, f, 'numpy')
f1_ = sp.lambdify(x, f1, 'numpy')
f2_ = sp.lambdify(x, f2, 'numpy')

# Newton-Raphson algoritması
x_val = 3.0  # Başlangıç değeri
iteration = 0

print(f"-- {iteration}  x: {x_val:.6f}  f: {f_(x_val):.6f}  f1: {f1_(x_val):.6f}  f2: {f2_(x_val):.6f}")

while abs(f1_(x_val)) > 1e-10:
    iteration += 1
    dx = -f1_(x_val) / f2_(x_val)
    x_val = x_val + dx

    print(f"-- {iteration}  x: {x_val:.6f}  f: {f_(x_val):.6f}  f1: {f1_(x_val):.6f}  f2: {f2_(x_val):.6f}  dx: {dx:.6f}")
