#include <stdio.h>
#include <ctype.h>

typedef struct Node {
	int data;
	struct Node* left;
	struct Node* right;
}Tree;

Tree tree[1100];
Tree *que[1100];
int res[1100];

int main() {
	int i, n, t, a, b;
	int idx, qsize;
	char c;
	Tree *root;
	while(scanf("%d", &n) != EOF) {
		for(i = 1; i <= n; i++) {
			scanf("%d", &t);
			tree[i].data = t;
			tree[i].left = NULL;
			tree[i].right = NULL;
			que[i] = NULL;
		}
		root = &tree[1];
		for(i = 1; i <= n; i++) {
			while((c = getchar()) && !isalpha(c));
			if(c == 'd') {
				scanf("%d %d", &a, &b);
				tree[i].left = &tree[a];
				tree[i].right = &tree[b];
			}
			if(c == 'l') {
				scanf("%d", &a);
				tree[i].left = &tree[a];
			}
			if(c == 'r') {
				scanf("%d", &b);
				tree[i].right = &tree[b];
			}
		}
		que[1] = root;
		idx = qsize = i = 1;
		while(que[i] != NULL) {
			if(que[i]->left) {
				que[qsize + 1] = que[i]->left;
				qsize++;
			}
			if(que[i]->right) {
				que[qsize + 1] = que[i]->right;
				qsize++;
			}
			res[idx++] = que[i]->data;
			i++;
		}
		idx = 1;
		for(i = 1; i < n; i++) {
			printf("%d ", res[i]);
		}
		printf("%d\n", res[n]);
	}
}