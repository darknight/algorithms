#include <stdio.h>
#include <math.h>

int main() {
	int i, n, max;
	scanf("%d", &n);
	max = (int)pow(10, n) - 1;
	for(i = 1; i <= max; i++) {
		printf("%d\n", i);
	}
}