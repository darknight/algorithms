#include <stdio.h>
#include <string.h>

int main() {

	char str[35];
	int big[35], div[10];
	int n, i, j, k;

	while(fgets(str, 34, stdin)) {
		if(str[0] == '-') break;
		n = strlen(str)-1;//discard '\n'
		for(i = 0; i < n; i++)
			big[i] = str[i] - '0';
		j = 0;
		for(k = 2; k <= 9; k++) {
			int sum = 0;
			for(i = 0; i < n; i++) {
				sum = (sum * 10 + big[i]) % k;
			}
			if(sum == 0)
				div[j++] = k;
		}
		if(j) {
			for(i = 0; i < j - 1; i++)
				printf("%d ", div[i]);
			printf("%d\n", div[i]);
		}
		else printf("none\n");
	}

	return 0;
}
