#include <stdio.h>

long long fab[100];

int main() {
	int i, n;
	fab[0] = 0;
	fab[1] = 1;
	for(i = 2; i < 100; i++) {
		fab[i] = fab[i-1] + fab[i-2];
	}
	while(scanf("%d", &n) != EOF) {
		printf("%lld\n", fab[n]);
	}
}