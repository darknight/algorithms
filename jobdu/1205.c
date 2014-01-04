#include <stdio.h>

int main() {

	long long f[128];
	int n;
	f[1] = 1;
	f[2] = 2;
	while(scanf("%d", &n) != EOF) {
		int i;
		for(i = 3; i <= n; i++)
			f[i] = f[i-1] + f[i-2];
		printf("%lld\n", f[n]);
	}
	return 0;
}
