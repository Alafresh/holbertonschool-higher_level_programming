#include "lists.h"

/**
* middle_list - find the middle of a linked list
* @head: linked list
* Return: the middle
*/

listint_t *middle_list(listint_t **head)
{
	listint_t *slow = (*head);
	listint_t *fast = (*head);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}

/**
* is_palindrome - function that checks if a singly linked list is a palindrome
* @head: address of a linked list
* Return: 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *middle = middle_list(head);

	if ((*head) == NULL)
		return (1);
	while (middle != NULL)
	{
		if (middle->n != (*head)->n)
			return (1);
		(*head) = (*head)->next;
		middle = middle->next;
	}
	return (0);
}
