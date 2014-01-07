#include <stdio.h>

int seq[11000];
int flag;

void check(start, end) {
	if(end - start < 3) return;
	int root = seq[end];
	int i, j;
	for(i = start; i < end; i++) {
		if(seq[i] > root) break;
	}
	j = i - 1;
	for(; i < end; i++) {
		if(seq[i] < root) {
			flag = 0;
			break;
		}
	}
	if(flag) {
		check(start, j);
		check(j + 1, end - 1);
	}
}

int main() {
	int i, j, n;
	while(scanf("%d", &n) != EOF) {
		for(i = 0; i < n; i++) {
			scanf("%d", &seq[i]);
		}
		flag = 1;
		check(0, n - 1);
		if(flag) printf("Yes\n");
		else printf("No\n");
	}
}