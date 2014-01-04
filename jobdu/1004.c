#include <stdio.h>
#include <stdlib.h>

int main() {

	long int *a, *b;
	int m, n, index;
	int i, j, k;

	while(scanf("%d", &m) != EOF) {
		a = (long int *)malloc(m * sizeof(long int));
		for(i = 0; i < m; i++) {
			scanf("%ld", a+i);
		}
		scanf("%d", &n);
		b = (long int *)malloc(n * sizeof(long int));
		for(i = 0; i < n; i++) {
			scanf("%ld", b+i);
		}
		
		index = (m+n+1)/2 - 1;
		i = j = k = 0;
		while(i < m && j < n) {// boundary !!!
			if(k == index) {
				printf("%ld\n", a[i] <= b[j] ? a[i] : b[j]);
				break;
			}
			else k++;
			if(a[i] <= b[j])  i++;
			else  j++;
		}
		if(j >= n) printf("%ld\n", a[i + index - k]);
		if(i >= m) printf("%ld\n", b[j + index - k]);
		free(a);
		free(b);
	}
}