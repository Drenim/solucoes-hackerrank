#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int num_of_tests, i, j;
    scanf("%d",&num_of_tests);
    int m[num_of_tests][4];
    for(i = 0; i < num_of_tests; i++){
        scanf("%d %d %d %d", &m[i][0], &m[i][1], &m[i][2], &m[i][3]);
    }
    for(i = 0; i < num_of_tests; i++){
        printf("%d %d \n",2*m[i][2]-m[i][0], 2*m[i][3]-m[i][1]);
    }
        return 0;
}
