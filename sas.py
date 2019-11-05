P = int()
Q = int()
sup = int()
N = float(0)
seriesK = []
H = float(0)
P = int(input(">>>insert P:\n>>>"))
Q = int(input(">>>insert Q:\n>>>"))

coord1 = (1 / (2 * Q), 1 / (2 * Q))
coord2 = (1 / (2 * P), - (1 / (2 * P)))
#я так до конца и не понял зачем нам нужны эти координаты, но пусть будут
sup = int(2 * Q - 1)            #supremum series
for n in range(sup):            #here sum N 
    if n == 0:
        k = 1
        N += k
        seriesK.append(k)
    if n >= 1 and n <= (Q - 1):
        k = 1 + 2 * ((P * n)/Q)
        N += k
        seriesK.append(k)
    if n == Q:
        k = 2 * P - 1
        N += k
        seriesK.append(k)
    if n >= (Q + 1) and n <= (sup):
        k = 1 + 2 * (2 * P - (P * n)/Q)
        N += k
        seriesK.append(k)
for n in range(sup):
    for k in seriesK:
        H += (9 / N) * ( ((1 - n / Q) ** 2) - ((k / P) ** 2) ) ** 2
print(H)
print(P, Q, sup, N)
print(seriesK) 
print(2*P*Q, N)
print(coord1, coord2)