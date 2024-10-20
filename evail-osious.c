#include<stdio.h>
int main(){
    int N, count, temp_ones;
    printf("Enter a positive integer: ");
    scanf("%d", &N);
    temp_ones = N;
    count = 0;
    //printf("temp_ones = %d   count= %d\n", temp_ones, count);
    while(temp_ones>0){
        if(temp_ones%2 == 1){
            count++;
            //printf("in the while : temp_ones = %d   count= %d\n", temp_ones, count);
        }
        temp_ones/=2;
    }
    //printf("temp_ones = %d   count= %d\n", temp_ones, count);
    if(count%2==0){
        printf("%d is an Odious number.\n", N);
    }
    else{
        printf("%d s a Evil number.\n", N);
    }

    return 0;
}

/*
// sample output:
Enter a positive integer: 3
3 is an Odious number.

Enter a positive integer: 2
2 s a Evil number.

Enter a positive integer: 10
10 is an Odious number.



*/
