#include <stdio.h>
#include <stdlib.h>

int arr[110000];
/*
void quick_sort(int *a, int s, int t) {
	int i = s, j = t;
	int piovt = a[j];
	if(s >= t) return;
	while(i < j) {
		while(i < j && a[i] <= piovt) i++;
		if(i < j) {
			a[j] = a[i];
			j--;
		}
		while(i < j && a[j] >= piovt) j--;
		if(i < j) {
			a[i] = a[j];
			i++;
		}
	}
	a[i] = piovt;
	quick_sort(a, s, i - 1);
	quick_sort(a, i + 1, t);
}
*/

int cmp(const void *a, const void *b) {
	return *(int *)a - *(int *)b;
}

int main() {
	int i, n;
	while(scanf("%d", &n) != EOF) {
		for(i = 0; i < n; i++) {
			scanf("%d", &arr[i]);
		}
		qsort(arr, n, sizeof(int), cmp);
		/*
		quick_sort(arr, 0, n-1);
		*/
		/*
		for(i = 0; i < n - 1; i++) {
			printf("%d ", arr[i]);
		}
		printf("%d\n", arr[n-1]);
		//*/
		int t = arr[n / 2];
		int k = 0;
		for(i = 0; i < n; i++) {
			if(arr[i] == t) k++;
		}
		if(k > n / 2) printf("%d\n", t);
		else printf("-1\n");
	}
}