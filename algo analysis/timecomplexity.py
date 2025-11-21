#time complexity handbook!

# O(1) 
def c1(a):
    return a[0] - only runs once.

# O(n)
def c2(n):
    for _ in range(n):
        pass - #n times 

# O(a+b) - esentially o(n)
def c3(a, b):
    for _ in a: pass
    for _ in b: pass

# O(log n)
def c4(n):
    i = 1
    for _ in range(999999999):   # dummy upper bound
        if i >= n: break
        i *= 2 # same outcome for i=i/2. 

# O(log log n)
def c5(n):
    i = 2
    for _ in range(999999999):
        if i >= n: break
        i = i*i 

# O(sqrt n)
def c6(n):
    r = int(n**0.5)
    for _ in range(r):
        pass 

# O(n log n)
def c7(n):
    for _ in range(n):
        j = 1
        for _ in range(999999999):
            if j >= n: break
            j *= 2

# O(n^2)
def c8(n):
    for i in range(n):
        for j in range(n):
            pass

# O(n^2) triangular
def c9(n):
    for i in range(n):
        for j in range(i, n):
            pass

# O(n log n) harmonic
def c10(n):
    for i in range(1, n+1):
        j = 1
        for _ in range(999999999):
            if j > n: break
            j += i

# O(n^3)
def c11(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass

# O(sqrt n) shrinking
def c12(n):
    step = int(n**0.5)
    for _ in range(n//step + 1):
        pass

# O(1) best, O(n) worst
def c13(a, x):
    for v in a:
        if v == x: return True
    return False

# O(2^n)
def c14(n):
    if n == 0: return 1
    return c14(n-1) + c14(n-1)

# O(n)
def c15(n):
    if n == 0: return 1
    return 1 + c15(n-1)

# O(log n)
def c16(a, l, r, x):
    if l > r: return -1
    m = (l+r)//2
    if a[m] == x: return m
    if x < a[m]: return c16(a, l, m-1, x)
    return c16(a, m+1, r, x)

# O(n log n)
def c17(n):
    if n <= 1: return 1
    return c17(n//2) + c17(n//2)
