from ffi_examples import py, cy, nim, rs, c, cpp

def test_names():
    for _ in range(1000000):
        assert py() == "Python"
        assert cy() == "Cython"
        assert nim() == "Nim"
        assert rs() == "Rust"
        assert c() == "C"
        assert cpp() == "C++"