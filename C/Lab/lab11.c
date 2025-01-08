#include <stdio.h>
#include <math.h>

void main(){
    float A[50], sum, sumvar, mean, var, sd;
    float *ptr;
    int n;

    printf("Enter the number of elements: ");
    scanf("%d",&n);

    printf("Enter the elements:\n");
    for (int i=0; i<n; i++){
        scanf("%f",&A[i]);
    }

    ptr=A;

    for (int i=0; i<n; i++){
        sum += *ptr;
        ptr++;
    }

    mean = sum/n;
    ptr = A;

    for (int i=0; i<n; i++){
        sumvar += pow((*ptr-mean),2);
        ptr++;
    }

    var = sumvar/n;
    sd = sqrt(var);

    printf("Sum = %f\n",sum);
    printf("Mean = %f\n",mean);
    printf("Standard Deviation = %f\n",sd);

}