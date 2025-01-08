#include <stdio.h>
#define MAX 50

void display(int Arr[MAX][MAX], int row, int col){
    for (int i=0; i<row; i++){
        for (int j=0; j<col; j++){
            printf(" %d |",Arr[i][j]);
        }
        printf("\n");
    }
}

void main(){
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];
    int row1=1, col1=1, row2=1, col2=1;

    printf("Enter Matrix A dimension: ");
    scanf("%dx%d",&row1,&col1);

    printf("Enter Matrix B dimension: ");
    scanf("%dx%d",&row2,&col2);

    printf("Enter Matrix A elements:\n");
    for (int i=0; i<row1; i++){
        for (int j=0; j<col1; j++){
            scanf("%d", &A[i][j]);
        }
    }

    printf("Enter Matrix B elements:\n");
    for (int i=0; i<row2; i++){
        for (int j=0; j<col2; j++){
            scanf("%d", &B[i][j]);
        }
    }

    printf("Matrix A:\n");
    display(A, row1, col1);

    printf("\nMatrix B:\n");
    display(B, row2, col2);

    printf("\nMatrix Multiplication:\n");

    for (int i=0; i<row1; i++){
        for (int j=0; j<col2; j++){
            C[i][j] = 0;
            for (int k=0; k<col1; k++){
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    display(C, row1, col2);

}