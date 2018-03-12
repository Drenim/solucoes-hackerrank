#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int num_of_tests, i;
    scanf("%d", &num_of_tests);
    int v[num_of_tests];
    for (i = 0; i < num_of_tests; i++){
        scanf("%d",&v[i]);
        v[i]++;
    }
    for(i = 0; i < num_of_tests; i++) printf("%d\n",v[i]);
    return 0;
}
