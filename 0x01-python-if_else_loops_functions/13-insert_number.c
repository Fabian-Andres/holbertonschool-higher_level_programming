#include "lists.h"
/**
 * insert_node - Insert head
 * @head: Head to insert
 * @number: to insert
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *aux_head = NULL;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL || head == NULL)
		return (NULL);

	aux_head = *head;

	if (number == 0)
	{
		new_node->n = number;
		new_node->next = aux_head;

		*head = new_node;
		return (new_node);
	}

	while ((aux_head->next)->n < number && aux_head->next != NULL)
	{
		if (aux_head == NULL)
			return (NULL);
		aux_head = aux_head->next;
	}

	new_node->n = number;
	new_node->next = aux_head->next;

	aux_head->next = new_node;

	return (new_node);
}
