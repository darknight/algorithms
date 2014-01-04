#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct TreeNode{
	char data;
	struct TreeNode *left;
	struct TreeNode *right;
}Tree;

Tree* insert(char c, Tree* t) {

	if(t == NULL) {
		t = (Tree *)malloc(sizeof(Tree));
		t->data = c;
		t->left = t->right = NULL;
	}
	else if(t->data > c)
		t->left = insert(c, t->left);
	else t->right = insert(c, t->right);

	return t;
}

void empty(Tree *t) {

	if(t != NULL) {
		empty(t->left);
		empty(t->right);
		free(t);
	}
}

int equal(Tree *t1, Tree *t2) {

	if(t1 == NULL && t2 == NULL)
		return 1;
	else if(t1 && t2 && t1->data == t2->data &&
		     equal(t1->left, t2->left) && equal(t1->right, t2->right)) {
		return 1;
	}
	else return 0;
}

int main() {

	char a[15], b[15];
	Tree *t1 = NULL;
	Tree *t2 = NULL;
	int n, i, j, k;

	while(scanf("%d", &n), n) {
		getchar();
		fgets(a, 15, stdin);
		k = strlen(a);
		for(i = 0; i < k-1; i++) {
			t1 = insert(a[i], t1);
		}
		for(i = 0; i < n; i++) {
			fgets(b, 15, stdin);
			k = strlen(b);
			for(j = 0; j < k-1; j++)
				t2 = insert(b[j], t2);
			if(equal(t1, t2))
				printf("YES\n");
			else printf("NO\n");
			empty(t2);
			t2 = NULL;
		}
		empty(t1);
		t1 = NULL;
	}
	return 0;
}
