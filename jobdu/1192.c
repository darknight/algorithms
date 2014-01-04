#include <stdio.h>
#include <string.h>

int main() {

	char str[1024];
	int i, j, len, find;
	while(fgets(str, 1023, stdin) != NULL) {
		len = strlen(str);
		i = 0;
		j = len - 2;
		find = 1;
		while(i < j) {
			if(str[i] != str[j]) {
				find = 0;
				break;
			}
			i++;
			j--;
		}
		if(find) printf("Yes!\n");
		else printf("No!\n");
	}
	return 0;
}
