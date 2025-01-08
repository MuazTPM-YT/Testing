#include <stdio.h>

int length(char str[]){
    int count=0;
    for (int i=0; str[i]!='\0'; i++){
        count++;
    }
    return count;
}

void compare(char str1[], char str2[]){
    int flag = 1;

    if (length(str1) != length(str2)){
        flag = 0;
    }

    else {
        for (int i=0; str1[i]!='\0'; i++){
            if (str1[i] != str2[i]){
                flag = 0;
                break;
            }
        }   
    }

    if (flag==1){
        printf("Strings are Same\n");
    }
    else {
        printf("Strings are different\n");
    }
}

void concatenate(char str1[], char str2[]){
    int i = length(str1);
    for (int j=0; str2[j]!='\0'; j++){
        str1[i] += str2[j];
        i++;
    }
    printf("Concatenated String: %s\n",str1);
}

void main(){
    char str1[50], str2[50];

    printf("String 1: ");
    scanf("%s",str1);

    printf("String 2: ");
    scanf("%s",str2);

    int len1 = length(str1);
    int len2 = length(str2);

    printf("\nLength of String 1: %d\n", len1);
    printf("Length of String 2: %d\n", len2);

    compare(str1,str2);
    concatenate(str1,str2);
}