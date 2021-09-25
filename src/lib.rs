use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
 
#[pyfunction]
fn run() -> &'static str {
    println!("Rust");
    "Rust"
}
 
/// A Python module implemented in Rust.
#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(run))?;
 
    Ok(())
}