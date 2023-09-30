#include "lists.h"


int is_palindrome(listint_t **head)
{
	/* if palindrome return 1 */
	/* if not palindrome return 0 */
	/* loop through the list forward and backwards */
	/* if the characters dont match, it is not a palindrome*/


	listint_t *stack = malloc(sizeof(listint_t));
	listint_t *node = NULL;
	int node2;

	if (head == NULL || *head == NULL)
		return (1);

	node = *head;

	/* loop through the linked list */
	while (node)
	{
		/* add the node to the stack */
		add_nodeint_end(&stack, node->n);
		node = node->next;
	}

	node = *head;

	while (node)
	{
		node2 = pop(&stack);
		if (node2 != node->n)
			return(0);
		node = node->next;
	}

	free_listint(stack);
	return (1);
}


/**
 * delete_dnodeint_at_index - deletes a node at an index
 *
 * @head: head of a dlistint_t list.
 * @index: indext of the node to delete.
 *
 * Return: sum of elements
 */
int pop(listint_t **head)
{
	listint_t *node = NULL, *prev = NULL;
	int data;

	if (head == NULL || *head == NULL)
		return (-1);

	if ((*head)->next == NULL)
	{
		data = (*head)->n;
		free(*head);
		*head = NULL;
	}

	else
	{
		prev = *head;
		node = (*head)->next;
		while(node)
		{
			if (node->next == NULL)
			{
				data = node->n;
				free(node);
				prev->next = NULL;
				break;
			}
			prev = node;
			node = node->next;
		}
	}

	return (data);
}
