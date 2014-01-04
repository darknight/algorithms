#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main() {

	char str[81];
	int i, n;

	while(fgets(str, 80, stdin)) {
		n = strlen(str);
		if(str[0] == '!' && n == 2) break;
		for(i = 0; i < n; i++) {
			if(isupper(str[i]))
				str[i] = 'A' + 'Z' - str[i];
			else if(islower(str[i]))
				str[i] = 'a' + 'z' - str[i];
		}
		printf("%s", str);
	}
}
