#include<stdio.h>
int main()
{
    float h,w;
    printf("Enter height and weight:");
    scanf("%f %f",&h,&w);
    float x=h*12*0.0254;
    float bmi=w/(x*x);
    printf("the Bmi is %f \n",bmi);

    if(bmi<18.5)
    {
        printf("underweight");
    }
    else if(bmi>=18.5 && bmi<=24.9)
    {
        printf("Normal weight");
    }
    return 0;
}