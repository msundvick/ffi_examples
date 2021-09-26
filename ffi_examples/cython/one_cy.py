import cython

@cython.ccall
def run():
    _run()
    return "Cython"

@cython.cfunc
def _run():
    a: cython.double = 0
    i: cython.int
    for i in range(1_000_000):
        a += (i % 2) - 0.5
    print(a)