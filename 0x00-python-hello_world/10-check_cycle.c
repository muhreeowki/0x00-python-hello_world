#include "lists.h"

/**
 * find_listint_loop - finds a cycle in a linked list
 *
 * @head: Head of the linked list
 *
 * Return: address of where cycle occures
 */
int check_cycle(listint_t *list)
{
	listint_t *pointer1 = NULL, *pointer2 = NULL;

	if (list)
	{
		pointer1 = pointer2 = list;

		if (list->next && list->next->next && list == list->next->next)
			return (1);

		while (pointer2 != NULL && pointer2->next != NULL)
		{
			pointer1 = pointer1->next;
			pointer2 = pointer2->next->next;

			if (pointer1 == pointer2)
				return (1);
		}
	}
	return (0);
}
