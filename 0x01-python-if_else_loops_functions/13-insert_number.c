#include "lists.h"
/**
 * insert_node - inserts a new node into a sorted list
 * @head: pointer to head pointer
 * @number: number to add to list
 * Return: new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new, *h;

	if (!head)
		return (NULL);
	h = *head;
	prev = h;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!h)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	while (h->n < number)
	{
		prev = h;
		h = h->next;
	}
	new->next = prev->next;
	prev->next = new;
	return (new);

}
