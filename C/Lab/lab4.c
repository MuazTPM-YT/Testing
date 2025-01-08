#include <stdio.h>

void main(){
    int row;

    printf("Enter the number of row(s): ");
    scanf("%d",&row);

    for (int i=1; i<=row; i++){
        for (int j=1; j<=row-i; j++){
            printf(" ");
        }
        for (int j=1; j<=i; j++){
            printf("%d",j);
        }
        for (int j=i-1; j>=1; j--){
            printf("%d",j);
        }
        printf("\n");
    }
}