#include <stdio.h>

int eat()
{
    return 0;
}
int sleep()
{
    return 0;
}
int code()
{
    return 0;
}
int repeat()
{
    return 0;
}

void main()
{
    int alive = 1;

    while (alive)
    {
        eat();
        sleep();
        code();
        repeat();
    }
}