#include <stdio.h>

int main() {

	int n, m[4][5], t[2][5];
	int i, j, p, q, max, max2;

	scanf("%d", &n);
	while(n--) {
		for(i = 0; i < 4; i++)
			scanf("%d %d %d %d %d", m[i]+0, m[i]+1, m[i]+2, m[i]+3, m[i]+4);
		for(j = 0; j < 5; j++) {
			p = m[0][j] >= m[1][j] ? 0 : 1;
			q = m[2][j] >= m[3][j] ? 2 : 3;
			max = m[p][j] >= m[q][j] ? p : q;
			if(max == p) {
				max2 = m[1-p][j] >= m[q][j] ? (1-p) : q;
			}
			else
				max2 = m[p][j] >= m[5-q][j] ? p : (5-q);
			t[0][j] = max;
			t[1][j] = max2;
			if(max > max2) {
				t[0][j] = max2;
				t[1][j] = max;
			}
		}
		for(i = 0; i < 2; i++)
			printf("%d %d %d %d %d \n", m[t[i][0]][0], m[t[i][1]][1],
					m[t[i][2]][2], m[t[i][3]][3], m[t[i][4]][4]);
	}
}
