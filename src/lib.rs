use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
 
#[pyfunction]
fn run() -> &'static str {
    let mut a: f64 = 0.0;
    for i in 0..1_000_000 {
        a += (i % 2) as f64 - 0.5
    }

    println!("{}", a.to_string());
    "Rust"
}
 
/// A Python module implemented in Rust.
#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(run))?;
 
    Ok(())
}