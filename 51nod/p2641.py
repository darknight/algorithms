import math

def calculate_m_z(n):
    z = 1
    while True:
        total = 2 * n + 6 * z
        m = int(math.sqrt(total))
        if m * (m + 1) == total:
            print("%d %d" % (z, m))
            return
        z += 1


T = input()
for _ in range(int(T)):
    n = int(input())
    calculate_m_z(n)

if __name__ == '__main__':
    pass