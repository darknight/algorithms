#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char hash[100100];

int toInt(char *s, int n) {

	int num = 0;
	int sz = strlen(s);
	if(sz > 6) return 0;
	num = atoi(s);
	if(num > 0 && num <= n)
		return num;
	return 0;
}

int main() {

	int n, i, j, count;
	char str[128];

	while(scanf("%d", &n) != EOF) {
		memset(hash, 0, 100100);
		count = 0;
		for(i = 0; i < n; i++) {
			scanf("%s", str);
			j = toInt(str, n);
			if(j) {
				if(hash[j])
					count++;
				else
					hash[j] = 1;
			}
			else
				count++;
		}
		printf("%d\n", count);
	}
	return 0;
}
