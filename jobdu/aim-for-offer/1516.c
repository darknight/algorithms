#include <stdio.h>

#define N 1000000

int a1[N];
int a2[N];
int a3[N];

int main() {
	int n, i, j, k;
	scanf("%d", &n);
	for(i = 0; i < n; i++) {
		scanf("%d", &a1[i]);
	}
	i = j = k = 0;
	for(; i < n; i++) {
		if(a1[i] % 2) {
			a2[j++] = a1[i];
		}
		else {
			a3[k++] = a1[i];
		}
	}
	for(i = 0; i < j; i++) {
		printf("%d ", a2[i]);
	}
	for(i = 0; i < k - 1; i++) {
		printf("%d ", a3[i]);
	}
    printf("%d\n", a3[k-1]);
}