#include <stdio.h>
#include <string.h>

#define M 10
#define N 10

int main() {

	int A[M+N] = {0};
	int item, m, n, i, j;
	int sum = 0;

	scanf("%d", &m);
	while(m != 0) {
		scanf("%d", &n);
		for(i = 0; i < 2*m; i++) {
			for(j = 0; j < n; j++) {
				scanf("%d", &item);
				A[i < m ? i : i - m] += item;
				A[j+m] += item;
			}
		}
		for(i = 0; i < m+n; i++) {
			if(A[i] == 0)
				sum++;
		}
		printf("%d\n", sum);
		memset(A, 0, M+N);
		sum = 0;
		scanf("%d", &m);
	}
}