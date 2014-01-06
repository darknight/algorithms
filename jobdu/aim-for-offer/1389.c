#include <stdio.h>

int main() {
	int n;
	while(scanf("%d", &n) != EOF) {
		printf("%lld\n", (long long)1 << (n - 1));
	}
}