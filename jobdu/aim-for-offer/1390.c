#include <stdio.h>

long long fab[100];

int main() {
	int i, n;
	fab[1] = 1;
	fab[2] = 2;
	for(i = 3; i < 100; i++) {
		fab[i] = fab[i-1] + fab[i-2];
	}
	while(scanf("%d", &n) != EOF) {
		printf("%lld\n", fab[n]);
	}
}