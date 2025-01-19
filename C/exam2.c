#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){    
    char str1[10]="Hello", str2[10]="World";
    printf("%s\n",str1);
    strcat(str1,str2);
    printf("%s",str1);
    return 0;
}