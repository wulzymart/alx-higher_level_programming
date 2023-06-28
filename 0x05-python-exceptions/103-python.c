#include "Python.h"
/**
 * print_python_bytes - prints a python byte object
 * @p: python Object
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, limit;
	char *str;
	int i;

	puts("[.] bytes object info");
	if PyBytes_Check(p)
	{
		size = ((PyVarObject *)p)->ob_size;
		printf("  size: %ld\n", size);
		str = ((PyBytesObject *)p)->ob_sval;
		printf("  trying string: %s\n", str);
		limit = size < 10 ? size + 1 : 10;
		printf("  first %ld bytes: ", limit);
		for (i = 0 ; i <  limit ; i++)
		{
			printf("%02hhx", str[i]);
			if (i < limit - 1)
				putchar(' ');
			else
				putchar('\n');
		}
	}
	else
		puts("  [ERROR] Invalid Bytes Object");
}
/**
 * print_python_float - prints a float object
 * @p: python object
*/
void print_python_float(PyObject *p)
{
	double x;
	char *x_str;

	puts("[.] float object info");
	if PyFloat_Check(p)
	{
		x = ((PyFloatObject *)p)->ob_fval;
		x_str = PyOS_double_to_string(x, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", x_str);
		PyMem_Free(x_str);
	}
	else
		puts("  [ERROR] Invalid Float Object");
}
/**
 * print_python_list - prints a python list object
 * @p: python Object
*/
void print_python_list(PyObject *p)
{
	PyListObject *tmp;
	Py_ssize_t alloc, size;
	PyObject *item;

	puts("[*] Python list info");
	if (PyList_Check(p))
	{
		size = ((PyVarObject *)p)->ob_size;
		tmp = (PyListObject *)p;
		alloc = tmp->allocated;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", alloc);
		for (int i = 0; i < size; i++)
		{
			item = PyList_GET_ITEM(p, i); /* Can't fail */
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			if PyFloat_Check(item)
				print_python_float(item);
		}
	}
	else
		puts("  [ERROR] Invalid List Object");
}
