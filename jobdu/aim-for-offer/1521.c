#include <stdio.h>
#include <ctype.h>

typedef struct Node {
	int data;
	struct Node* left;
	struct Node* right;
}Tree;

Tree tree[1100];
int res[1100];
int idx;

void mirror(Tree *t) {
	Tree *tmp;
	if(t == NULL) return;
	mirror(t->left);
	mirror(t->right);
	tmp = t->left;
	t->left = t->right;
	t->right = tmp;
}

void print_preorder(Tree *t) {
	if(t == NULL) return;
	res[idx++] = t->data;
	print_preorder(t->left);
	print_preorder(t->right);
}

int main() {
	int i, n, t, a, b;
	char c;
	Tree *root;
	while(scanf("%d", &n) != EOF) {
		if(n == 0) {
			printf("NULL\n");
			continue;
		}
		for(i = 1; i <= n; i++) {
			scanf("%d", &t);
			tree[i].data = t;
			tree[i].left = NULL;
			tree[i].right = NULL;
		}
		root = &tree[1];
		for(i = 1; i <= n; i++) {
			while((c = getchar()) && !isalpha(c));
			//printf("c = %c\n", c);
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
		mirror(root);
		idx = 1;
		print_preorder(root);
		for(i = 1; i < n; i++) {
			printf("%d ", res[i]);
		}
		printf("%d\n", res[n]);
	}
}