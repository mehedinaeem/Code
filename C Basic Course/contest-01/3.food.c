
#include <stdio.h>
int main()
{
    int rack_num;
    printf("Enter rack Number:");
    scanf("%d", &rack_num);

    long long int total_food = 0;
    for (int i = 1; i <= rack_num; i++)
    {
        
        int food_number;
        scanf("%d", &food_number);

        total_food = total_food + food_number;
        printf("For loop %d Toatal_food=%lld and food_number=%d\n", i, total_food, food_number);
        printf("\n");
    }
    printf("Out of loop total food=%lld\n", total_food);

    return 0;
}