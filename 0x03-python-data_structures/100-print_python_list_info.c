#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python list object
*/
void print_python_list_info(PyObject *p)
{
	long len;
	int i;
	PyListObject *list;
	PyObject *obj;

	if (p)
	{
		len = PyList_Size(p);
		list = (PyListObject *)p;

		printf("[*] Size of the Python List = %li\n", len);
		printf("[*] Allocated = %li\n", list->allocated);
		for (i = 0; i < len; i++)
		{
			obj = PyList_GetItem(p, i);
			printf("Element %i: %s\n", i, Py_TYPE(obj)->tp_name);
		}
	}
}
