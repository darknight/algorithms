#include <stdio.h>
#include <string.h>

#define N 1000

int dfs(int v, int (*p)[N], int *visited, int sz) {

	int w;
	if(visited[v]) return 0;
	visited[v] = 1;
	for(w = 1; w <= sz; w++) {
		if(p[v][w])
			dfs(w, p, visited, sz);
	}
	return 1;
}

int main() {

	int n, m, k;
	int i, j;
	int v, w;
	int city[N][N], cp[N][N];//1 ... n
	int visited[N];

	memset(city, 0, N * N * sizeof(int));
	scanf("%d %d %d", &n, &m, &k);
	for(i = 0; i < m; i++) {
		scanf("%d %d", &v, &w);
		city[v][w] = city[w][v] = 1;
	}
	for(i = 0; i < k; i++) {
		scanf("%d", &v);
		memset(visited, 0, N * sizeof(int));
		memcpy(cp, city, N * N * sizeof(int));
		for(w = 1; w <= n; w++) {
			if(cp[v][w])
				cp[v][w] = cp[w][v] = 0;
		}
		j = 0;
		for(w = 1; w <=n; w++) {
			if(dfs(w, cp, visited, n))
				j++;
		}
		printf("%d\n", j-2);
	}
}
