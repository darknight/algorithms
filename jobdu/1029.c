#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define N 100100
#define M 110000

const char *end = "@END@\n";
char word[N][25], expr[N][85]; // fine, pretty good ...
int hw[M], he[M];

unsigned int bkdrHash(char *str) {

	unsigned int seed = 131; // 31, 131, 1313, 13131 ...
	unsigned int hash = 0;
	while(*str){
		hash = hash * seed + *str++;
	}
	return (hash & 0x7FFFFFFF) % M; // mod !!
}

int setPos(int idx, int arr[]) {

	int i = 1;
	while(arr[idx]) {
		idx = (idx + i * i) % M;
		i++;
	}
	return idx;
}

int getPos(int idx, int arr[], int who, char *str) {

	int i = 1, k = 0;
	while(arr[idx]) {
		if(who == 0 && strcmp(word[arr[idx]], str) == 0) {
			k = hw[idx];
			break;
		}
		else if(who && strcmp(expr[arr[idx]], str) == 0) {
			k = he[idx];
			break;
		}
		else {
			idx = (idx + i * i) % M;
			i++;
		}
	}
	return k;
}

int main() {

	//char word[100000][25], exp[100000][85];// segmentation fault !!
	char w[128];
	int i, j, k, n;

	k = 1;
	memset(hw, 0, M * sizeof(int));
	memset(he, 0, M * sizeof(int));
	while(fgets(w, 127, stdin)) {
		if(strcmp(w, end) == 0)
			break;
		assert(w[0] == '[');
		i = 0;
		while(w[i] != ']') {
			word[k][i] = w[i];
			i++;
		}
		word[k][i++] = ']';
		word[k][i++] = '\n';
		word[k][i] = '\0';
		j = setPos(bkdrHash(word[k]), hw);
		hw[j] = k;

		j = 0;
		while(expr[k][j++] = w[i++]) ;
		j = setPos(bkdrHash(expr[k]), he);
		he[j] = k;

		k++;
	}
	scanf("%d", &n);
	getchar();
	while(n--) {
		fgets(w, 127, stdin);
		if(w[0] == '[') {
			j = getPos(bkdrHash(w), hw, 0, w);
			if(j)
				printf("%s", expr[j]);
			else
				printf("what?\n");
		}
		else {
			j = getPos(bkdrHash(w), he, 1, w);
			if(j) {
				k = strlen(word[j]);
				for(i = 1; i < k-2; i++)
					printf("%c", word[j][i]);
				printf("\n");
			}
			else
				printf("what?\n");
		}
	}
	return 0;
}
