#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list is circular
 * @list: linked list object
 *
 * Return: 0 if there is no cycle or 1
 */
int check_cycle(listint_t *list)
{
        listint_t *slow, *fast;

        slow = fast = list;

        while (slow && fast && fast->next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return (1);
        }
        return (0);
}
