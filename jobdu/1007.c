#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef	struct {
	int id;
	int medal[2];
	double ratio[2];
	int pop;
}country;

int main() {

	int m, n;
	int i, j, k;
	int id, min, chosen;
	while(scanf("%d %d", &n, &m) != EOF) {
		country *tmp = (country *)malloc(n * sizeof(country));
		country *coun = (country *)malloc(m * sizeof(country));
		int **rank = (int **)malloc(m * sizeof(int *));
		for(i = 0; i < m; i++) {
			rank[i] = (int *)malloc(4 * sizeof(int));
			for(j = 0; j < 4; j++)
				rank[i][j] = 1;
		}
		for(i = 0; i < n; i++) {
			scanf("%d %d %d", &tmp[i].medal[0], &tmp[i].medal[1], &tmp[i].pop);
			tmp[i].ratio[0] = tmp[i].medal[0] / (double) tmp[i].pop;
			tmp[i].ratio[1] = tmp[i].medal[1] / (double) tmp[i].pop;
			tmp[i].id = i;
		}
		for(i = 0; i < m; i++) {
			scanf("%d", &chosen);
			memcpy(coun + i, tmp + chosen, sizeof(country));
		}
		for(j = 0; j < 2; j++)
			for(i = 0; i < m; i++)
				for(k = 0; k < m; k++)
					if(i != k && coun[i].medal[j] < coun[k].medal[j])
						rank[i][j]++;
		for(j = 0; j < 2; j++)
			for(i = 0; i < m; i++)
				for(k = 0; k < m; k++)
					if(i != k && coun[i].ratio[j] < coun[k].ratio[j])
						rank[i][j+2]++;
		for(i = 0; i < m; i++) {
			min = rank[i][0] <= rank[i][1] ? 0 : 1;
			min = rank[i][min] <= rank[i][2] ? min : 2;
			min = rank[i][min] <= rank[i][3] ? min : 3;
			printf("%d:%d\n", rank[i][min], min+1);
		}
		printf("\n");
		free(tmp);
		free(coun);
		for(i = 0; i < m; i++)
			free(rank[i]);
		free(rank);
	}
	return 0;
}
