#include <stdio.h>

int arr[1100000];

int main() {
	int n, i, min;
	while(scanf("%d", &n) != EOF) {
		for(i = 0; i < n; i++) {
			scanf("%d", &arr[i]);
		}
		min = arr[0];
		for(i = 1; i < n; i++) {
			if(arr[i] < min) {
				min = arr[i];
			}
		}
		printf("%d\n", min);
	}
}