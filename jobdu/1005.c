#include <stdio.h>
#include <stdlib.h>

#define N 40000
#define K 5

typedef struct {
	int id;
	int ge;
	int gi;
	int final;
	int choice[K];
}applicant;

typedef struct {
	int sum;
	int limit;
	//int p[N];
	int p[N];
}school;

int cmp(const void *p, const void *q) {

	applicant *a = (applicant *)p;
	applicant *b = (applicant *)q;

	if(a->final != b->final) return b->final - a->final;
	else return b->ge - a->ge;
}

int cmp2(const void *p, const void *q) {
	return *(int *)p - *(int *)q;
}

int main() {

	int n, k, m;
	int i, j;
	applicant *app;
	school *sch;
	int t;


	while(scanf("%d %d %d", &n, &m, &k) != EOF) {
		sch = (school *)malloc(m * sizeof(school));
		for(i = 0; i < m; i++) {
			scanf("%d", &sch[i].limit);
			sch[i].sum = 0;
		}
		app = (applicant *)malloc(n * sizeof(applicant));
		for(i = 0; i < n; i++) {
			scanf("%d %d", &app[i].ge, &app[i].gi);
			app[i].id = i;
			app[i].final = (app[i].ge + app[i].gi) / 2;
			for(j = 0; j < k; j++)
				scanf("%d", &app[i].choice[j]);
		}
		qsort(app, n, sizeof(applicant), cmp);
		for(i = 0; i < n; i++) {
			for(j = 0; j < k; j++) {
				t = app[i].choice[j];
				if(sch[t].sum < sch[t].limit) {
					sch[t].p[sch[t].sum++] = i;
					break;
				}
				else if(app[sch[t].p[sch[t].sum-1]].final == app[i].final &&
								app[sch[t].p[sch[t].sum-1]].ge == app[i].ge) {
					sch[t].p[sch[t].sum++] = i;
					break;
				}
			}
		}
		for(i = 0; i < m; i++) {
			for(j = 0; j < sch[i].sum; j++) sch[i].p[j] = app[sch[i].p[j]].id;
			qsort(sch[i].p, sch[i].sum, sizeof(int), cmp2);
			for(j = 0; j < sch[i].sum - 1; j++) {
				printf("%d ", sch[i].p[j]);
			}
			if(j < sch[i].sum)
				printf("%d\n", sch[i].p[j]);
			else
				puts("");
		}
	}
	return 0;
}
