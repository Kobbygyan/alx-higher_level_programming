/*
 * File: 103-python.c
 * Auth: Kwabena Gyan-Kyereko
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, type);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    char *data = PyBytes_AsString(p);

    printf("[.] Bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", data);

    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx", data[i]);
        if (i + 1 < size && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid PyFloatObject\n");
        return;
    }

    double value = PyFloat_AsDouble(p);

    printf("[.] Float object info\n");

    printf("  value: %.17g\n", value);
}
