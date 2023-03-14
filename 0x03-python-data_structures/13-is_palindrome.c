#include "lists.h"
/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *mid1, *mid2;
	listint_t *fwd, *bck;
	int len, i;

	if (*head == NULL)
		return (1);
	bck = *head;
	len = 0;
	while (fwd != NULL)
	{
		fwd = bck->next;
		bck = fwd;
		len++;
	}
	mid1 = *head;
	mid2 = (*head)->next;
	i = 1;

	while (i < (len / 2))
	{
		mid1 = mid2;
		mid2 = mid1->next;
		i++;
	}

	bck = reverse_listint(&mid2);
	mid2 = bck;
	mid1 = *head;

	while (mid1 != NULL && mid2 != NULL)
	{
		if (mid1->n != mid2->n)
			return (0);
		bck = mid1->next;
		mid1 = bck;
		fwd = mid2->next;
		mid2 = fwd;
	}
	return (1);
}
