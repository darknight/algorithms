#include <stdio.h>
#include <stdlib.h>

int cmp(const void *p, const void *q) {

	return *(int *)q - *(int *)p;
}

int main() {

	int  *rich, n, m;
	int i;

	while(scanf("%d %d", &n, &m) && n && m) {
		rich = (int *)malloc(n * sizeof(int));
		for(i = 0; i < n; i++)
			scanf("%d", rich + i);
		qsort(rich, n, sizeof(int), cmp);
		m = m <= n ? m : n;
		for(i = 0; i < m-1; i++) {
			printf("%d ", rich[i]);
		}
		printf("%d\n", rich[i]);
		free(rich);
	}
}
