#include "lists.h"

/**
 * list_len - gets the length of a list
 * @head: head pointer
 * Return: length of list
*/
int list_len(listint_t *head)
{
	int len = 0;

	while (head)
	{
		len++;
		head = head->next;
	}
	return (len);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head pointer
 * Return: 0 (false) or 1 (true)
*/
int is_palindrome(listint_t **head)
{
	int *list_arr, i = 0, j = 0;
	listint_t *h;

	if (!head || !*head)
		return (0);
	if (!(*head)->next)
		return (1);
	h = *head;
	list_arr = malloc(sizeof(int) * list_len(*head));
	if (!list_arr)
		return (0);
	while (h)
	{
		list_arr[i++] = h->n;
		h = h->next;
	}
	i--;
	while (j < i)
	{
		if (list_arr[j++] != list_arr[i--])
		{
			free(list_arr);
			return (0);
		}
	}
	free(list_arr);
	return (1);
}
