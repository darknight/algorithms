#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int data;
	int left;
	int right;
}Tree;

Tree nodes[2000];
int preorder[2000];
int postorder[2000];
int invalid;

int rebuild(int i, int j, int start, int end) {
	int k = 0, find = 0;
	if(i > j || start > end) return -1;
	if(j - i != end - start) return -1;
	int root = preorder[i];
	for(k = start; k <= end; k++) {
		if(root == nodes[k].data) {
			find = 1;
			break;
		}
	}
	if(find == 0) {
		invalid = 1;
		return -1;
	}
	nodes[k].left = rebuild(i + 1, i + k - start, start, k - 1);
	nodes[k].right = rebuild(i + k - start + 1, j, k + 1, end);
	return k;
}

void traverse_postorder(int h) {
	if(nodes[h].left != -1) traverse_postorder(nodes[h].left);
	if(nodes[h].right != -1) traverse_postorder(nodes[h].right);
	printf("%d ", nodes[h].data);
}

int main() {
	int i, n, head;
	while(scanf("%d", &n) != EOF) {
		for(i = 0; i < n; i++) {
			scanf("%d", &preorder[i]);
		}
		for(i = 0; i < n; i++) {
			scanf("%d", &nodes[i].data);
			nodes[i].left = -1;
			nodes[i].right = -1;
		}
		invalid = 0;
		head = rebuild(0, n-1, 0, n-1);
		if(invalid == 1) {
			printf("No\n");
		}
		else {
			traverse_postorder(head);
			printf("\n");
		}
	}
}
