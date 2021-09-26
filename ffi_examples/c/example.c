#include <stdio.h>
#include <Python.h>

static PyObject *_run(PyObject *self)
{
    double a = 0;
    int i;
    for (i = 0; i < 1000000; i++)
    {
        a += i % 2 - 0.5;
    }
    printf("%f\n", a);

    return PyUnicode_FromString("C");
}

static struct PyMethodDef methods[] = {
    {"run", (PyCFunction)_run, METH_NOARGS},
    {NULL, NULL}};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "c_example",
    "Hi",
    -1,
    methods};

PyMODINIT_FUNC PyInit_c_example(void)
{
    return PyModule_Create(&module);
}