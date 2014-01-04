#include <stdio.h>
#include <math.h>

int main() {

	long long n, tmp;
	double k;
	long long res;

	while(scanf("%lld", &n) != EOF) {
		k = sqrt(n << 1);
		res = floor(k);
		tmp = (res + 1) * res / 2;
		if(tmp < n) res++;
		printf("%lld\n", res);
	}
	return 0;
}
