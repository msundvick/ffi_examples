from ffi_examples import py, cy, nim, rs

def test_names():
    assert py() == "Python"
    assert cy() == "Cython"
    assert nim() == "Nim"
    assert rs() == "Rust"