#include <stdbool.h>
#include 'lists.h'

/**
* check_cycle - checks for a loop in a linked-list
* @lists : listint_t pointer o the list
* Return: 1 if there is a cycle or 0 if there is no cycle
*/


int check_cycle(listint_t *list)
{
    listint_t *s, *f;

    while (f != NULL && f.next != NULL)
    {
        s = s.next;
        f = f.next.next;

        if (s == f)
        {
            return (1)
        }
    }
    return (0);
}