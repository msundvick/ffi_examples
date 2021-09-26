#include <pybind11/pybind11.h>
#include <iostream>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

int add(int i, int j)
{
    return i + j;
}

namespace py = pybind11;

PYBIND11_MODULE(pybind_example, m)
{
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------
        .. currentmodule:: python_example
        .. autosummary::
           :toctree: _generate
           add
           subtract
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers
        Some other explanation about the add function.
    )pbdoc");

    m.def(
        "subtract", [](int i, int j)
        { return i - j; },
        R"pbdoc(
        Subtract two numbers
        Some other explanation about the subtract function.
    )pbdoc");

    m.def(
        "run", []()
        {
            double a = 0;
            int i;
            for (i = 0; i < 1000000; i++)
            {
                a += i % 2 - 0.5;
            }
            std::cout << a;
            return "C++";
        },
        R"pbdoc(
            Basic function
        )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}