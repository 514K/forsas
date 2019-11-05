import math
P = float()
Q = float()
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
for n in range(sup+1): 
    # print(n)           #here sum N 
    if n == 0:
        k = 1
        N += k
        seriesK.append(k)
    if n >= 1 and n <= (Q - 1):
        k = 1 + 2 * (math.ceil((P * n) / Q) - 1)
        # print(math.ceil((P * n) / Q), k)
        N += k
        seriesK.append(k)
    if n == Q:
        k = 2 * P - 1
        N += k
        seriesK.append(k)
    if n >= (Q + 1) and n <= (sup):
        k = 1 + 2 * (math.ceil(2 * P - (P * n)/Q) - 1)
        # print(math.ceil(2 * P - (P * n)/Q), k)
        N += k
        seriesK.append(k)
for n in range(2 * Q):
    H += ( (1 - n/Q)*(1 - n/Q) - (seriesK[n]/P)*(seriesK[n]/P) )*( (1 - n/Q)*(1 - n/Q) - (seriesK[n]/P)*(seriesK[n]/P) )


H = (9 / N) * H
print("H =", H)
print("P =", P,"Q =", Q,"n максимально достигает 2Q-1 =", sup)
print("Список всех к для Bn:", seriesK) 
print("2PQ =", 2*P*Q,"N =", N)
print(coord1, coord2)
input()