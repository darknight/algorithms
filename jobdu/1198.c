#include <stdio.h>
#include <string.h>

#define N 1024

int main() {

	char a[N], b[N], c;
	int i, j, k, tmp;

	while(scanf("%s %s", a, b) != EOF) {
		i = strlen(a);
		j = strlen(b);
		if(i < j) {
			for(k = 0; k <= i; k++) {
				c = a[k];
				a[k] = b[k];
				b[k] = c;
			}
			for( ; k <= j; k++) a[k] = b[k];
			tmp = i;
			i = j;
			j = tmp;
		}
		i -= 1;
		j -= 1;
		k = 0;
		while(i >= 0 && j >= 0) {
			tmp = (a[i] - '0') + (b[j] - '0') + k;
			k = tmp / 10;
			a[i] = tmp % 10 + '0';
			i--;
			j--;
		}
		while(i >= 0) {
			if(k == 0) break;
			tmp = (a[i] - '0') + k;
			k = tmp / 10;
			a[i] = tmp % 10 + '0';
			i--;
		}
		if(k) printf("1");
		printf("%s\n", a);
	}
	return 0;
}
