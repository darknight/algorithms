#include <stdio.h>
#include <stdlib.h>

int comp(const void *a, const void *b) {
	int *p = (int *)a;
	int *q = (int *)b;//(int *)q?? stupid!
	return *q - *p;
}

int main() {

	int nodes[1001], n, i, j, sum;

	while(scanf("%d", &n) != EOF) {
		for(i = 0; i < n; i++)
			scanf("%d", nodes+i);
		sum = 0;
		qsort(nodes, n, sizeof(int), comp);
		while(n > 1) {
			j = nodes[n-1] + nodes[n-2];
			sum += j;
			nodes[n-2] = j;
			n--;
			for(i = n-1; i > 0; i--) {
				if(nodes[i-1] < nodes[i]) {
					j = nodes[i];
					nodes[i] = nodes[i-1];
					nodes[i-1] = j;
				}
			}
			
		}
		printf("%d\n", sum);
	}
	return 0;
}