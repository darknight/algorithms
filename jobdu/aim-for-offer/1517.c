#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int data;
	struct Node* next;
}LList;

int main() {
	int i, n, k, t;
	LList *head, *tail, *p;
	while(scanf("%d %d", &n, &k) != EOF) {
		head = tail = p = NULL;
		for(i = 0; i < n; i++) {
			scanf("%d", &t);
			p = (LList *)malloc(sizeof(LList));
			p->data = t;
			p->next = NULL;
			if(head == NULL) {
				head = p;
				tail = p;
			}
			else {
				tail->next = p;
				tail = p;
			}
		}
		if(n < k || k == 0 || n == 0) printf("NULL\n");
		else{
			t = n - k;
			p = head;
			for(i = 0; i < t; i++) {
				p = p->next;
			}
			printf("%d\n", p->data);
		}
		while(head) {
			p = head;
			head = head->next;
			free(p);
		}
	}
}