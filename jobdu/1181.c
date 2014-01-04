#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int data;
	struct node *next;
}List;

int main() {

	int i, n, k;
	List *curr, *p;

	while(scanf("%d", &n) != EOF) {
		List head = {0, NULL};
		for(i = 0; i < n; i++) {
			scanf("%d", &k);
			curr = (List *)malloc(sizeof(List));
			curr->data = k;
			curr->next = NULL;
			p = &head;
			while(p->next) {
				if(p->next->data > curr->data) break;
				p = p->next;
			}
			curr->next = p->next;
			p->next = curr;
		}
		if(n == 0) continue;
		p = head.next;
		while(p->next) {
			printf("%d ", p->data);
			p = p->next;
		}
		printf("%d\n", p->data);
		p = head.next;
		while(p) {
			curr = p;
			p = p->next;
			free(curr);
		}
	}
}
