#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int w;
	int v;
	double unit;
}jew_t;

jew_t jew[100001];

int comp(const void *a, const void *b) {

	jew_t *p = (jew_t *)a;
	jew_t *q = (jew_t *)b;
	//return p->unit - q->unit; // from big to small
	//return q->unit * 1E2 - p->unit * 1E2; //passed case 1, 2
	//return q->unit * 1E6 - p->unit * 1E6; //passed case 3, 4, 5, 6
	if(q->unit > p->unit) return 1;
	if(q->unit < p->unit) return -1;
	return 0;
}

int main() {

	int n, c;
	int i;
	double sum;
	while(scanf("%d", &n) != EOF) {
		scanf("%d", &c);
		for(i = 0; i < n; i++) {
			scanf("%d %d", &jew[i].w, &jew[i].v);
			jew[i].unit = 1.0 * jew[i].v / jew[i].w;
		}
		qsort(jew, n, sizeof(jew_t), comp);
		//for(i = 0; i < n;i ++)
		//	printf("%d 's unit = %.2f\n", i, jew[i].unit);
		sum = 0.0;
		i = 0;
		while(c > 0 && i < n) {
			if(c >= jew[i].w) {
				sum += jew[i].v;
				c -= jew[i].w;
				i++;
				//printf("sum = %.2f, c = %d\n", sum, c);
			}
			else {
				sum += c * jew[i].unit;
				c = 0;
				i++;
				//printf("sum = %.2f, c = %d\n", sum, c);
			}
		}
		printf("%d\n", (int)(sum + 0.5));
	}
}
