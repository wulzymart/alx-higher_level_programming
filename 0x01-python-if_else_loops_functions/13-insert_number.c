#include "lists.h"
/**
 * insert_node - inserts a new node into a sorted list
 * @head: pointer to head pointer
 * @number: number to add to list
 * Return: new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL, *new, *h;

	if (!head)
		return (NULL);
	h = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	while (h && h->n < number)
	{
		prev = h;
		h = h->next;
	}
	if (!prev)
	{
		new->next = h;
		*head = new;
		return (new);
	}
	new->next = prev->next;
	prev->next = new;
	return (new);

}
