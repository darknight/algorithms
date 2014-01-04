#include <stdio.h>
#include <stdlib.h>

int matrix[1100][1100];
int m, n, t;

int cmp(const void *a, const void *b){
    return *(int*)a - *(int*)b; 
}

int main() {
    int i = 0, j = 0, isIn = 0;
    while(scanf("%d %d", &m, &n) != EOF) {
        isIn = 0;
        scanf("%d", &t);
        for(i = 0; i < m; i++)
            for(j = 0; j < n; j++)
                scanf("%d", &matrix[i][j]);
        for(i = 0; i < m; i++) {
            if(matrix[i][n-1] > t) break;
        }
        for(i = 0; i < m; i++) {
            if(bsearch(&t, matrix[i], n, sizeof(int), cmp)) {
                isIn = 1;
                break;
            }
        }
        if(isIn == 1) {
            printf("Yes\n");
        }
        else {
            printf("No\n");
        }
    }
}
