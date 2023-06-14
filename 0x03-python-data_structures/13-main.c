#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head, *head2, *new;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 5);
    add_nodeint_end(&head, 7);
    print_listint(head);
    head2 = NULL;
    add_nodeint_end(&head2, 2);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 6);
    add_nodeint_end(&head, 8);
    print_listint(head2);
    

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}
