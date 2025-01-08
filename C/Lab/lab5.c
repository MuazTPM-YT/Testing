#include <stdio.h>
#include <stdlib.h>

void main(){
    int A[50], key, n;

    printf("Number of Elements: ");
    scanf("%d",&n);


    printf("\nEnter %d Elements:\n",n);
    for (int i=0; i<n; i++){
        scanf("%d",&A[i]);
    }

    printf("\nKey: ");
    scanf("%d",&key);

    int low = 0;
    int high = n-1;

    while (low<=high){
        int mid = (low+high)/2;

        if (A[mid]==key){
            printf("Element found at %d\n",mid+1);
            exit(0);
        }
        else if (A[mid]>key){
            high = mid-1;
        }
        else {
            low = mid+1;
        }
    }

    printf("Element not found\n");
}