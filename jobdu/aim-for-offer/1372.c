#include <stdio.h>

int arr[110000];
int max[110000];
int idx[110000];

int main() {
	int m, n, i, j, s;
	while(scanf("%d", &n) != EOF) {
		if(n == 0) break;
		for(i = 0; i < n; i++)
			scanf("%d", &arr[i]);
		max[0] = arr[0];
		idx[0] = 0;
		for(i = 1; i < n; i++) {
			if(max[i-1] + arr[i] < arr[i]) {
				max[i] = arr[i];
				idx[i] = i;
			}
			else{
				max[i] = arr[i] + max[i-1];
				idx[i] = idx[i-1];
			}
		}
		m = max[0];
		i = idx[0];
		for(j = 1; j < n; j++) {
			if(max[j] > m) {
				m = max[j];
				i = idx[j];
			}
		}
		s = arr[i];
		j = i;
		while(s != m) s += arr[++j];
		printf("%d %d %d\n", m, i, j);
	}
}