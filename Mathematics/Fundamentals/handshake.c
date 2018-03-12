#include <stdio.h>
#include <stdlib.h>

int fatorialuntilp(int n, int p){
    int i, tot = 1;
    if (p + 1 == n) return n;
    for (i = n; i >= p + 1; i--)
        tot *= i;
    return tot;
}
int combinacao(int n, int p){
    if (n < p) return 0;
    if (n == 0 || p == 0) return 1;
    return fatorialuntilp(n, n - p) / p;
}
int main() {
    int T, i;
    int *v;
    scanf("%d",&T);
    v = malloc(T * sizeof (int));
    for (i = 0; i < T; i++){
        scanf("%d",&v[i]);
        v[i] = combinacao(v[i], 2);
    }
    for (i = 0; i < T; i++) printf("%d\n",v[i]);
    free(v);
    v = NULL;
}
