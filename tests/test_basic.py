from ffi_examples import py, cy, nim, rs, c, cpp, jl
jl()

N = 1000
def test_py():
    for _ in range(N):
        assert py() == "Python"
def test_cy():
    for _ in range(N):
        assert cy() == "Cython"
def test_nim():
    for _ in range(N):
        assert nim() == "Nim2"
def test_rs():
    for _ in range(N):
        assert rs() == "Rust"
def test_c():
    for _ in range(N):
        assert c() == "C"
def test_cpp():
    for _ in range(N):
        assert cpp() == "C++"
def test_jl():
    for _ in range(N):
        assert jl() == "Julia"