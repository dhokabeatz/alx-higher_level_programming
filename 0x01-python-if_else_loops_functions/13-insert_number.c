#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: NULL if the function fails, or a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
