# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 11:42:05 2025

@author: pc
"""

import math

# Altın oran sabiti
phi = (1 + math.sqrt(5)) / 2

# Hedef fonksiyonu tanımla
def f(x):
    return (x - 2*x + x + 1)**2 + (x + x - x + 3)** + (-2*x + x - x)**2
# Altın oran 
def golden_section_search(f, a, b, tol=0.0001):
    iterasyon = -1
    # İlk iki iç nokta
    c = b - (b - a) / phi
    d = a + (b - a) / phi
    while abs(b - a) > tol:
        iterasyon += 1
        if f(c) < f(d):
            b = d
        else:
            a = c

        # Yeni c ve d değerleri
        c = b - (b - a) / phi
        d = a + (b - a) / phi

    x_min = (b + a) / 2
    return x_min, f(x_min), iterasyon

# Altın oranla çöz
a, b = 0, 4
x_min, f_min, iters = golden_section_search(f, a, b)

print(f"Minimum noktası: x = {x_min:.5f}")
print(f"Minimum değeri: f(x) = {f_min:.5f}")
print(f"Toplam iterasyon sayısı: {iters}")
