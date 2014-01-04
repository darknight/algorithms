#include <stdio.h>

int main() {

	int i, j;
	int card[14];
	int tri, pir, u, v;

	while(scanf("%d", card) != EOF) {
		for(i = 1; i <= 13; i++)
			card[i] = 0;
		u = v = 0;
		for(i = 0; i < card[0]; i++) {
			scanf("%d", &j);
			card[j]++;
		}
		scanf("%d %d %d %d %d", &tri, &tri, &tri, &pir, &pir);
		if(tri == 2) {
			printf("My God\n");
			continue;
		}
		else if(tri == 1) {
			if(card[2] >= 3) u = 2;
		}
		else {
			for(i = tri + 1; i <= 13; i++) {
				if(card[i] >= 3) {
					u = i;
					break;
				}
			}
		}
		if(!u) {
			if(card[2] >= 3) u = 2;
			if(card[1] >= 3) u = 1;
		}
		if(!u) {
			printf("My God\n");
			continue;
		}
		for(i = 3; i <= 13; i++) {
			if(card[i] >= 2 && i != u) {
				v = i;
				break;
			}
		}
		if(!v && u != 1 && card[1] >= 2) v = 1;
		if(!v && u != 2 && card[2] >= 2) v = 2;
		if(!v) {
			printf("My God\n");
			continue;
		}
		printf("%d %d %d %d %d\n", u, u, u, v, v);
	}
}
