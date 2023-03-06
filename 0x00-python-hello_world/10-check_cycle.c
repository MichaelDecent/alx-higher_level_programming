#include "lists.h"
/**
 * check_cycle - a function in C that checks
 * if a singly linked list has a cycle in it
 * @list: the singly linked list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *head;
	int i;

	if (list == NULL)
		return (0);

	head = list;
	for (i = 0; list->next != NULL; i++)
	{
		if (list->next == head)
		{
			return (1);
		}
		temp = list->next;
		list = temp;
	}
	return (0);
}
