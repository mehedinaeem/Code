#include <stdio.h>

int main()
{
    while (1)
    {
        char op;
        printf("What to do: ");
        scanf(" %c", &op);  // Consume any leading whitespace, including newline characters

        if (op == '+')
        {
            int a, b;
            printf("Enter two numbers: ");
            scanf("%d %d", &a, &b);
            int sum = a + b;
            printf("The sum is %d\n", sum);
        }
        else if (op == '-')
        {
            int a, b;
            printf("Enter two numbers: ");
            scanf("%d %d", &a, &b);
            int sub = a - b;
            printf("The sub is %d\n", sub);
        }
        else if (op == '*')
        {
            int a, b;
            printf("Enter two numbers: ");
            scanf("%d %d", &a, &b);
            int multi = a * b;
            printf("The multiplication is %d\n", multi);
        }
        else if (op == '/')
        {
            int a, b;
            printf("Enter two numbers: ");
            scanf("%d %d", &a, &b);
            int div = a / b;
            printf("The division is %d\n", div);
        }
        else
        {
            printf("Operator not available.\n");
        }

        char checker;
        printf("Do you want to do more calculations (y/n): ");
        scanf(" %c", &checker);  // Consume any leading whitespace, including newline characters
        if (checker != 'y')
        {
            break;
            printf("The program is terminated");
        }
    }

    return 0;
}
