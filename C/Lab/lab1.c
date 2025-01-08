#include <stdio.h>

void main()
{
    int num1, num2, res;
    char op;

    printf(">>> ");
    scanf("%d%c%d", &num1, &op, &num2);

    switch (op)
    {
    case '+':
        res = num1 + num2;
        printf("Sum = %d", res);
        break;

    case '-':
        res = num1 - num2;
        printf("Difference = %d", res);
        break;

    case '*':
        res = num1 * num2;
        printf("Product = %d", res);
        break;

    case '/':
        if (num2 == 0)
        {
            printf("Division by Zero Error");
        }
        else
        {
            res = num1 / num2;
            printf("Quotient = %d", res);
        }
        break;

    case '%':
        if (num2 == 0)
        {
            printf("Division by Zero Error");
        }
        else
        {
            res = num1 % num2;
            printf("Remainder = %d", res);
        }
        break;

    default:
        printf("Invalid Expression\n");
    }
}