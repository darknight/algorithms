#include <stdio.h>
#include <string.h>

#define N 1000000
char text[N];

int main() {
	int i = 0;
	char c;
	while( (c = getchar()) != '\n') {
		if(c == ' ') {
			text[i] = '%';
			text[i+1] = '2';
			text[i+2] = '0';
			i += 3;
		}
		else{
			text[i] = c;
			i++;
		}
	}
	printf("%s\n", text);

	return 0;
}