#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int cap[1280];
	int st;
	int end;
	int last;
}window;

void toStr(int t) {
	int h = t / 60;
	int m = t % 60;
	if(t > 540) printf("Sorry\n");
	else printf("%02d:%02d\n", h+8, m);
}

int main() {

	int n, m, k, q;
	window win[32];
	int trans[1280], done[1280];
	int counter;
	int i, j, next, min, w;

	scanf("%d %d %d %d", &n, &m, &k, &q);
	for(i = 0; i < k; i++) {
		scanf("%d", &trans[i]);
		done[i] = 0;
	}
	for(j = 0; j < n; j++)
		win[j].st = win[j].last = win[j].end = 0;

	next = 0;
	for(i = 0; i < m; i++) {
		for(j = 0; j < n; j++) {
			if(next < k) {
				win[j].cap[i] = next++;
				win[j].end++;
			}
		}
	}

	counter = k;
	while(counter) {
		min = 0x7FFFFFFF;
		w = -1;
		for(j = 0; j < n; j++) {
			if(win[j].st == win[j].end) continue;
			i = win[j].cap[win[j].st];
			if(done[i] == 0) {
				done[i] = win[j].last + trans[i];
				win[j].last = done[i];
			}
			if(done[i] < min) {
				w = j;
				min = done[i];
			}
		}
		if(w != -1) {
			if(next < k) {
				win[w].cap[win[w].end++] = next++;
			}
			win[w].st++;
			counter--;
		}
	}

	for(i = 0; i < q; i++) {
		scanf("%d", &w);
		toStr(done[w - 1]);
	}
	return 0;
}
