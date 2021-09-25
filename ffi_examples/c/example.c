
#include <Python.h>

static PyObject *_run(PyObject *self)
{
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