#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int data;
	struct Node* next;
}LList;

void reverse_print(LList* p) {
	if(p->next) {
		reverse_print(p->next);
	}
	printf("%d\n", p->data);
}
int main() {
	LList *head = NULL, *p = NULL;
	int k = 0;
	while(scanf("%d", &k) != EOF) {
		if(k == -1) break;
		LList *t = (LList *)malloc(sizeof(LList));
		t->data = k;
		t->next = NULL;
		if(p) p->next = t;
		p = t;
		if(head == NULL) head = t;
	}
	reverse_print(head);
	return 0;
}