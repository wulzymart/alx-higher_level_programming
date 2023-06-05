#include "lists.h"
/**
 * check_cycle - checks for cycles in a linked list
 * @list: pointer of head node
 * Return: 1 if found, 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (!list || !list->next)
		return (0);
	while (slow && fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
