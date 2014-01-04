#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {

	int n;
	char arr[20][101];
	int i, j, k;
	int sum, tmp, len;

	scanf("%d", &n);
	for(i = 0; i < n; i++) {
		scanf("%s", arr[i]);
		sum = 0;
		len = strlen(arr[i]);
		j = 0;
		while(j < len) {
			if(!isdigit(arr[i][j])) j++;
			else {
				tmp = arr[i][j] - '0';
				k = j++;
				while(j < len) {
					if(isdigit(arr[i][j])) {
						tmp = 10 * tmp + arr[i][j] - '0';
						j++;
					}
					else break;
				}
				sum += tmp;
			}
		}
		printf("%d\n", sum);
	}
}
