#include <stdio.h>
#include <ctype.h>

int stack[11000];
int esp;

void push(int d) {
	stack[++esp] = d;
}

void pop() {
	if(esp >= 0)
		esp--;
}

void access() {
	if(esp < 0)
		printf("E\n");
	else
		printf("%d\n", stack[esp]);
}

int main() {

	int n;
	while(scanf("%d", &n) != EOF && n > 0) {
		int dt;
		char op, tmp;
		getchar();
		esp = -1;
		while(n--) {
			scanf("%c", &op);
			switch(op) {
				case 'A':
					access();
					tmp = getchar();
					break;
				case 'O':
					pop();
					tmp = getchar();
					while(tmp != '\n') tmp = getchar();
					break;
				case 'P':
					scanf("%d", &dt);
					push(dt);
					tmp = getchar();
					break;
			}
		}
		printf("\n");
	}
	return 0;
}
