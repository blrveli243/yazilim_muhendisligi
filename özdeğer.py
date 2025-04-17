
import numpy as np
from sympy import diff, symbols


# Sayfa 37'ye göre olan fonksiyon
def f(x1,x2,x3):
    return (x1 - 2*x2 + x3 + 1)**2 + (x1 + x2 - x3 + 3)**2 + (-2*x1 + x2 - x3)**2

# Verilen sembole göre türevi hesapla
def turev(f, sembol):
    return diff(f, sembol)


# Türevleri hesaplamak için semboller oluştur
x1,x2,x3 = symbols('x1 x2 x3')

# Fonksiyonu al
f = f(x1,x2,x3)

# İlk kısmi türevleri hesapla
df_dx1 = turev(f, x1)
df_dx2 = turev(f, x2)
df_dx3 = turev(f, x3)
print("x'e göre türev: ", df_dx1)
print("x2'ye göre türev: ", df_dx2)
print("x3e göre türev: ", df_dx2)

# İkinci kısmi türevleri hesapla
df_dx1dx1 = turev(df_dx, x)
df_dx1dx2 = turev(df_dx, y)

df_dydx = turev(df_dy, x)
df_dydy = turev(df_dy, y)


print("x^2'ye göre türev: ", df_dxdx)
print("x*y'ye göre türev: ", df_dxdy)

print("y*x'ye göre türev: ", df_dydx)
print("y^2'ye göre türev: ", df_dydy)

# İkinci kısmi türevler matrisini tanımla
# Not: özdeğerleri hesaplamak için türev dizisini float dizisine dönüştürün
H = np.matrix([[df_dxdx, df_dxdy], [df_dydx, df_dydy]]).astype(float)

print(" ", H)

# Özdeğerleri bul
ozdegerler = np.linalg.eig(H).eigenvalues

print("Özdeğerler:", ozdegerler)

# Bir tanesi negatif, diğeri pozitif
if (ozdegerler[0] * ozdegerler[1] < 0):
    print("Eğer noktası")

# İkisi de negatif
if (ozdegerler[0] < 0 and ozdegerler[1] < 0):
    print("Yerel maksimum noktası")

# İkisi de pozitif
print("Yerel minimum noktası")