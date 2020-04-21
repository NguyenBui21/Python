from time import time; t=time()


# 4(k-1)(a+b+c)+2(ab+bc+ca)+8(k-1)(k-2)/2

N = 1000
M = 20000

cache = [0] * M
for a in range(1, M):
    for b in range(1, a+1):
        ab = a * b
        if ab * 2 >= M: break
        a_b = a + b
        for c in range(1, b+1):
            s =(a_b * c + ab) * 2
            if s >= M: break
            cache[s] += 1
            ss = 4 * (a_b + c)
            for k in range(0, M, 8):
                s += ss + k
                if s >= M: break
                cache[s] += 1

for i, v in enumerate(cache):
    if v == N:
        break

print(i, time()-t)