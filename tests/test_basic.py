from ffi_examples import py, cy, nim, rs, c, cpp, jl

def test_names():
    for _ in range(100000):
        assert py() == "Python"
        assert cy() == "Cython"
        assert nim() == "Nim"
        assert rs() == "Rust"
        assert c() == "C"
        assert cpp() == "C++"
        assert jl() == "Julia"