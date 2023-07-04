#include "Python.h"
#include <wchar.h>
/**
 * print_python_string - prints Python strings.
 * @p: python object
*/
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	wchar_t *str;

	puts("[.] string object info");

	if PyUnicode_Check(p)
	{
		length = ((PyASCIIObject *)p)->length;
		if (PyUnicode_IS_COMPACT_ASCII(p))
			puts("  type: compact ascii");
		else
			puts("  type: compact unicode object");
		printf("  length: %ld\n", length);
		str = PyUnicode_AsWideCharString(p, &length);
		printf("  value: %ls\n",  str);
		PyMem_Free(str);
	}
	else
		puts("  [ERROR] Invalid String Object");
}
