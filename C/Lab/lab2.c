#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main(){
    float a,b,c,disc;

    printf("Enter the coefficients (a,b,c): ");
    scanf("%f, %f, %f",&a,&b,&c);

    if (a==0){
        if (b==0){
            printf("Roots can't be computed\n");
            exit(0);
        }
        else {
            float root = -c/b;
            printf("Roots are linear\n");
            printf("Root = %f\n",root);
            exit(0);
        }
    }

    disc = b*b - 4*a*c;

    if (disc==0){
        printf("\nRoots are real and equal\n");
        float root = (-b)/2*a;
        printf("Root 1 = Root 2 =%f\n",root);
    }

    else if (disc>0){
        printf("\nRoots are equal and distinct\n");
        float root1 = (-b + sqrt(disc))/2*a;
        float root2 = (-b - sqrt(disc))/2*a;
        printf("Root 1 = %f\n",root1);
        printf("Root 2 = %f\n",root2);
    }

    else {
        printf("\nRoots are complex and imaginary\n");
        float real = -b/(2*a);
        float img = sqrt(fabs(disc))/2*a;
        printf("Root 1 = %f + i%f\n",real, img);
        printf("Root 1 = %f - i%f\n",real, img);
    }
}