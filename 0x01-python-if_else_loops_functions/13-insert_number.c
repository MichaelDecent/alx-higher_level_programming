#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *prev;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return(NULL);
	}
	new_node->n = number;
	if (*head == NULL)
		*head = new_node;
	else
	{
		prev = *head;
		temp = prev->next;
		while(temp)
		{
			if ((prev->n < new_node->n) && (temp->n > new_node->n))
			{
				prev->next = new_node;
				new_node->next = temp;
				break;
			}
			prev = temp;
			temp = prev->next;
		}
	}
	return (new_node);


}
