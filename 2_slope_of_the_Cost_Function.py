# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy


def cost(b):
    return (b-4) ** 2
print(cost(4))
print(cost(55))

# numerically
def num_slope(b):
    h = 0.0001
    return (cost(b+h)-cost(b))/h

print(num_slope(3))
print(num_slope(4))
print(num_slope(55))

#calculsly
def slope(b):
    return 2*(b-4)

print("slpe 3 " ,slope(3))
print("slpe 4 " ,slope(4))
print("slpe 55 " ,slope(55))

# asıl tam olay budur oncekıler adım adımdı iterasyonla yaklasıyoruz 4 e yanı targeta iterasyon sonra eklendi
# usttekı 2 formulden biri kullanılarak yapılıyor bız burda slopeyi secdık num_slopede secılebılır
b = -20
b = b - .1 * slope(b)
print(b)

# bu iterasyonu asıl tamın usttekının yanı yawas yawas targeta yanı 4 e yaklasıyor (4 rastgele secılmıs bırtarget)
for i in range(200):
    b = b - .1 * slope(b)
    print(b)