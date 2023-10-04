#include "lists.h"

/**
 * check_cycle - checks whether the linked list contain cycle
 * @list: linked list
 * Return: int
 */

int check_cycle(listint_t *list)
{

	listint_t *temp = list;
	listint_t *temp2 = list;

	if (!list)
	{
		return (0);
	}

	while (temp2 && temp && temp2->next)
	{

		temp = temp->next;
		temp2 = temp2->next->next;
		if (temp == temp2)
			return (1);
	}
	return (0);
}
