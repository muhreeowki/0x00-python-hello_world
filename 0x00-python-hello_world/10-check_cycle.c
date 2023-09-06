#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 *
 * @list: Head of the linked list
 *
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	size_t count = 0;
	listint_t *item, **plist, *head = list;
	int i, loop = 0, start = 1;

	if (head == NULL)
		return (0);

	plist = make_pointer_list(head, NULL, 1);
	item = head;

	while (item != NULL && loop == 0)
	{
		for (i = 0; plist[i] != NULL; i++)
		{
			if (start == 1)
			{
				start = 0;
				break;
			}
			if (plist[i] == item)
				return (1);
		}
		count++;
		plist = make_pointer_list(item, plist, count);
		if (plist == NULL)
			exit(98);
		item = item->next;
	}
	return (0);
}

/**
 * make_pointer_list - adds a pointer to a list of pointers,
 * or creates a list of pointers if no list is provided.
 *
 * @pointer: pointer to be added
 * @list: list to append to
 * @count: number of items in the list
 *
 * Return: number of nodes
 */
listint_t **make_pointer_list(listint_t *pointer,
		listint_t **list, int count)
{
	listint_t **new_list = malloc(sizeof(listint_t **) * (count + 2));
	int i;

	/* if malloc fails */
	if (new_list == NULL)
	{
		free(list);
		return (NULL);
	}

	/*If list is empty*/
	if (list == NULL)
	{
		new_list[0] = pointer;
		new_list[1] = NULL;
		return (new_list);
	}

	/*loop through the old list, and */
	for (i = 0; i < count; i++)
	{
		/* copy the values from old list to new list */
		if (list[i] != NULL)
			new_list[i] = list[i];
	}

	/* add the new pointer to the list */
	new_list[i++] = pointer;
	new_list[i] = NULL;
	free(list);
	return (new_list);
}
