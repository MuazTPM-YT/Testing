#include <stdio.h>

struct Students {
    char name[100];
    int usn, marks;
};

void main(){
    struct Students s[50];
    int n;
    float sum;

    printf("Enter the number of students: ");
    scanf("%d",&n);

    printf("\nEnter Student Details:\n");
    printf("USN, Name, Marks:\n");
    for (int i=0; i<n; i++){
        scanf("%d %s %d", &s[i].usn, s[i].name, &s[i].marks);
        sum += s[i].marks;
    }

    float avg = sum/n;
    printf("Average: %f\n",avg);

    printf("Students who scored above average\n");
    for (int i=0; i<n; i++){
        if (s[i].marks >= avg){
            printf("%d, %s, %d", s[i].usn, s[i].name, s[i].marks);
            printf("\n");
        }
    }

    printf("Students who scored below average\n");
    for (int i=0; i<n; i++){
        if (s[i].marks < avg){
            printf("%d,%s,%d", s[i].usn, s[i].name, s[i].marks);
            printf("\n");
        }
    }
}