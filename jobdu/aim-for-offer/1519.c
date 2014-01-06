#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int data;
	struct Node* next;
}LList;

void print_list(LList* h) {
	LList *p = h;
	while(p->next) {
		printf("%d ", p->data);
		p = p->next;
	}
	printf("%d\n", p->data);
}

int main() {
	int i, n, m, t;
	LList *h1, *h2, *p, *q, *tail, *head;
	while(scanf("%d %d", &n, &m) != EOF) {
		h1 = tail = p = NULL;
		for(i = 0; i < n; i++) {
			scanf("%d", &t);
			p = (LList *)malloc(sizeof(LList));
			p->data = t;
			p->next = NULL;
			if(h1 == NULL) {
				h1 = p;
				tail = p;
			}
			else {
				tail->next = p;
				tail = p;
			}
		}
		h2 = tail = p = NULL;
		for(i = 0; i < m; i++) {
			scanf("%d", &t);
			p = (LList *)malloc(sizeof(LList));
			p->data = t;
			p->next = NULL;
			if(h2 == NULL) {
				h2 = p;
				tail = p;
			}
			else {
				tail->next = p;
				tail = p;
			}
		}
		if(m == 0 && n == 0) {
			printf("NULL\n");
			continue;
		}
		if(m == 0) {
			print_list(h1);
			continue;
		}
		if(n == 0) {
			print_list(h2);
			continue;
		}
		head = tail = NULL;
		while(h1 && h2) {
			if(h1->data <= h2->data) {
				if(head == NULL) {
					head = tail = h1;
				}
				else{
					tail->next = h1;
					tail = h1;
				}
				h1 = h1->next;
			}
			else{
				if(head == NULL) {
					head = tail = h2;
				}
				else{
					tail->next = h2;
					tail = h2;
				}
				h2 = h2->next;
			}
		}
		if(h1) tail->next = h1;
		if(h2) tail->next = h2;
		print_list(head);
		while(head) {
			p = head;
			head = head->next;
			free(p);
		}
	}
}