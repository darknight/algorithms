#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 2000

typedef struct {
	int id;
	int course[4];
}student;

int main() {

	student stu[N];
	int index[N][4];
	int i, j, k;
	char sym[4] = {'E', 'M', 'C', 'A'};
	int m, n;
	int tmp, aver;
	int min;

	scanf("%d %d", &n, &m);
	for(i = 0; i < n; i++) {
		scanf("%d %d %d %d", &stu[i].id, &stu[i].course[2], &stu[i].course[1], &stu[i].course[0]);
		aver = stu[i].course[2] + stu[i].course[1] + stu[i].course[0];
		stu[i].course[3] = (int)(aver/3.0 + 0.5); // shit! carry bit...
	}
	for(i = 0; i < N; i++)
		for(j = 0; j < 4; j++)
			index[i][j] = 1;
	for(j = 0; j < 4; j++) {
		for(i = 0; i < n; i++) {
			for(k = 0; k < n; k++) {
				if(i != k && stu[i].course[j] < stu[k].course[j])
					index[i][j]++;
			}
		}
	}
	for(i = 0; i < m; i++) {
		scanf("%d", &tmp);
		k = 0;
		for(j = 0; j < n; j++) {
			if(tmp == stu[j].id) {
				k = 1;
				if(index[j][1] <= index[j][0]) min = 1;
				else min = 0;
				if(index[j][2] <= index[j][min]) min = 2;
				if(index[j][3] <= index[j][min]) min = 3;
				break;
			}
		}
		if(k) printf("%d %c\n", index[j][min], sym[min]);
		else puts("N/A");
	}
	return 0;
}
