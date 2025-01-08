#include <stdio.h>
#include <math.h>

void main(){
    float x, degree, term, sum;
    int n;

    printf("Enter the number of terms: ");
    scanf("%d",&n);

    printf("\nEnter the degree: ");
    scanf("%f",&degree);

    x = degree * 3.141592 / 180;
    term = x;
    sum = x;

    for (int i=1; i<=n; i++){
        term = -term * x*x / (2*i*(2*i+1));
        sum += term;
    }

    printf("\nTaylor Series Approximation: %f\n", sum);
    printf("\nSine Value: %f\n", sin(x));
}