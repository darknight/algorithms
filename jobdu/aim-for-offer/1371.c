#include <stdio.h>

int heap[210000];

void heapify(int *heap, int i, int size) {
	int lchild = i * 2;
	int rchild = i * 2 + 1;
	int max = i, tmp;
	if(lchild <= size && heap[lchild] > heap[max])
		max = lchild;
	if(rchild <= size && heap[rchild] > heap[max])
		max = rchild;
	if(max != i) {
		tmp = heap[max];
		heap[max] = heap[i];
		heap[i] = tmp;
		heapify(heap, max, size);
	}
}

void buildheap(int *heap, int size) {
	int i;
	for(i = size / 2; i >= 1; i--) {
		heapify(heap, i, size);
	}
}

void heapsort(int *heap, int size) {
	int i, tmp;
	buildheap(heap, size);
	for(i = size; i >= 2; i--) {
		tmp = heap[1];
		heap[1] = heap[i];
		heap[i] = tmp;
		size--;
		heapify(heap, 1, size);
	}
}

int main() {
	int size, i, k;
	while(scanf("%d %d", &size, &k) != EOF) {
		for(i = 1; i <= size; i++) {
			scanf("%d", &heap[i]);
		}
		heapsort(heap, size);
		for(i = 1; i < k; i++) {
			printf("%d ", heap[i]);
		}
		printf("%d\n", heap[k]);
	}
}