cpdef run():
    return _run()
    
cdef _run():
    a: cython.double = 0
    for i in range(1_000_000):
        a += (i % 2) - 0.5
    print(a)
    return "Cython"