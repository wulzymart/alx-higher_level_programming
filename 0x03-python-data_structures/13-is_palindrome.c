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
	int i = 0, j, k;
	listint_t *left, *right;

	if (!head || !*head || !(*head)->next)
		return (0);
	j = list_len(*head) - 1;
	left = *head;

	while (i < j)
	{
		right = left;
		k = i;
		while (k < j)
		{
			right = right->next;
			k++;
		}
		if (left->n != right->n)
			return (0);
		left = left->next;
		i++;
		j--;
	}
	return (1);
}
