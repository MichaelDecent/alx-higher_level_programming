#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *prev;

	if (*head == NULL)
		return (1);
	temp = (*head)->next;
	prev = *head;

	while (temp != NULL)
	{
		if (prev->n == temp->n)
			return (1);
		prev = temp;
		temp = prev->next;
	}
	return (0);

}
