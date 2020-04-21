M = 1000

maxx = 0
ss = 0
for i in range(1, 31):
    nn = i*i
    for j in range(1, 2*i+1):
        n = nn + j
        if n > M: break
        p, q = i, j
        expan = [i]
        while True:
            r, s = 1, 0
            for k in expan:
                r, s = k*r+s, r
            if r*r - n*s*s == 1:
                if r > maxx:
                    ss = n
                    maxx = r
                break
            s = i + p
            k, p = s//q, s%q-i
            expan.insert(0, k)
            m = n - p*p
            assert m % q == 0
            p, q = -p, m//q
print(ss)