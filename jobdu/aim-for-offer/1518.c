#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int data;
	struct Node* next;
}LList;

int main() {
	int i, n, t;
	LList *head, *tail, *p, *q;
	while(scanf("%d", &n) != EOF) {
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
		if(n == 0) {
			printf("NULL\n");
			continue;
		}
		else if(n == 1) {
			printf("%d\n", head->data);
			free(head);
			continue;
		}
		else{
			p = NULL;
			q = head->next;
			while(q) {
				head->next = p;
				p = head;
				head = q;
				q = head->next;
			}
			head->next = p;
		}
		p = head;
		while(p->next) {
			printf("%d ", p->data);
			p = p->next;
		}
		printf("%d\n", p->data);
		while(head) {
			p = head;
			head = head->next;
			free(p);
		}
	}
}