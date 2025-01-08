#include <stdio.h>

void main(){
    int A[50], n;

    printf("Enter the elements of the array: ");
    scanf("%d",&n);

    printf("Enter Elements:\n");
    for (int i=0; i<n; i++){
        scanf("%d",&A[i]);
    }

    printf("Unsorted Array:\n");
    for (int i=0; i<n; i++){
        printf(" %d |",A[i]);
    } 

    for (int i=0; i<n-1; i++){
        for (int j=0; j<n-1-i; j++){
            if (A[j]>A[j+1]){
                int temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
            }
        }
    }

    printf("\nSorted Array:\n");
    for (int i=0; i<n; i++){
        printf(" %d |",A[i]);
    }
}