from ffi_examples import py, cy, nim, rs, c, cpp, jl

jl()

N = 1000


def test_py():
    for _ in range(N):
        assert py() == "Python"


def test_jl():
    for _ in range(N):
        assert jl() == "Julia"
