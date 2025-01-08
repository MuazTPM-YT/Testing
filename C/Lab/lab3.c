#include <stdio.h>

void main(){
    char name[30];
    int unit;
    float charge;

    printf("Enter Name: ");
    scanf("%s",name);

    printf("Enter Units: ");
    scanf("%d",&unit);

    if (unit <= 200){
        charge = (unit * 0.8) + 100;
    }

    if (unit <= 300){
        charge = (200 * 0.8) + ((unit-200) * 0.9) + 100;
    }

    if (unit > 300){
        charge = (200 * 0.8) + (100 * 0.9) + (unit-300) * 1 + 100;
    }

    if (charge > 400){
        charge += charge*0.15;
    }

    printf("\nName: %s",name);
    printf("\nUnits: %d",unit);
    printf("\nCharge: %f",charge);
}