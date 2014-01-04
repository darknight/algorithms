#include <stdio.h>
#include <stdlib.h>

int cmp(const void *p, const void *q) {

	return *(int *)p - *(int *)q;
}

int main() {

	int x[100], y[100];
	int i, n;

	while(1) {
		i = 0;
		scanf("%d %d", x+i, y+i);
		if(x[i] == 0 && y[i] == 0) break;
		while(x[i] || y[i]) {
			i++;
			scanf("%d %d", x+i, y+i);
		}
		n = i;
		qsort(x, n, sizeof(int), cmp);
		qsort(y, n, sizeof(int), cmp);
		printf("%d %d %d %d\n", x[0], y[0], x[n-1], y[n-1]);
	}
}
