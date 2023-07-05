#include "Python.h"
/**
 * print_python_string - prints Python strings.
 * @p: python object
*/
void print_python_string(PyObject *p)
{
	Py_ssize_t length;

	puts("[.] string object info");

	if PyUnicode_Check(p)
	{
		length = ((PyASCIIObject *)p)->length;
		if (PyUnicode_IS_COMPACT_ASCII(p))
			puts("  type: compact ascii");
		else
			puts("  type: compact unicode object");
		printf("  length: %ld\n", length);
		const char *str = PyUnicode_AsUTF8(p);
		printf("  value: %s\n",  str);
	}
	else
		puts("  [ERROR] Invalid String Object");
}
