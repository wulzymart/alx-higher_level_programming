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
 * is_palindrome1 - checks if a linked list is a palindrome
 * @head: pointer to head pointer
 * Return: 0 (false) or 1 (true)
*/
int is_palindrome1(listint_t **head)
{
	int *list_arr, i = 0, j = 0;
	listint_t *h;

	if (head && *head)
	{
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
		return (1);
}
/**
 * reverse - reverses a linked list
 * @head: pointer to head pointer
*/
void reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * compare_list - checks if values of 2 different lists are same
 * @a: head pointer of list a
 * @b: head pointer of list b
 * Return: 0 (false), 1 (true)
*/
int compare_list(listint_t **a, listint_t **b)
{
	listint_t *i = *a, *j = *b;

	while (i && j)
	{
		if (i->n != j->n)
			return (0);
		i = i->next;
		j = j->next;
	}
	return (1);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head pointer
 * Return: 0 (false) or 1 (true)
*/
int is_palindrome(listint_t **head)
{
	int result = 1;
	listint_t *fast, *slow, *prev_slow = NULL, *mid = NULL, *o_side;

	if (head && *head)
	{
		if (!(*head)->next)
			return (1);
		slow = *head;
		fast = *head;
		while (fast && fast->next)
		{
			prev_slow = slow;
			slow = slow->next;
			fast = fast->next->next;
		}
		if (fast)
		{
			mid = slow;
			slow = slow->next;
		}
		o_side = slow;
		prev_slow->next = NULL;
		reverse(&o_side);
		result = compare_list(head, &o_side);
		reverse(&o_side);
		if (mid)
		{
			prev_slow->next = mid;
			mid->next = o_side;
		}
		else
			prev_slow->next = o_side;
	}
	return (result);
}
