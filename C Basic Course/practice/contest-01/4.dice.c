#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int T, X, Y;
        scanf("%d%d", &X, &Y);
        T = X + Y;
        if (T > 6)
        {
            printf("YES\n");
        }
        else if (T <= 6)
        {
            printf("NO\n");
        }
    }
    return 0;
}
