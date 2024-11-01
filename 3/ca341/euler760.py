import sys

def bitwise(m, n):
    return (m & n) + (m | n) + (m ^ n)

N = int(sys.argv[1])

total = 0
for n in range(N + 1):
    for k in range(n + 1):
        total += bitwise(k, n - k)
print(total)