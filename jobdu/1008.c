#include <stdio.h>

#define N 1100
#define INF 0x7FFFFFFF

int dist[N], cost[N], known[N];
int dmap[N][N], cmap[N][N];

void dijkstra(int n, int s) {

	int i, v, w;
	int min;

	for(i = 1; i <= n; i++) {
		dist[i] = cost[i] = INF;
		known[i] = 0;
	}
	dist[s] = cost[s] = 0;

	while(1) {
		min = INF;
		for(i = 1; i <= n; i++) {
			if(!known[i] && dist[i] < min) {
				v = i;
				min = dist[i];
			}
		}
		if(min == INF) break;

		known[v] = 1;
		for(w = 1; w <= n; w++) {
			if(!known[w] && dmap[v][w] < INF) {
				if(dist[w] > dist[v]+dmap[v][w]) {
					dist[w] = dist[v] + dmap[v][w];
					cost[w] = cost[v] + cmap[v][w];
				}
				else if(dist[w] == dist[v]+dmap[v][w]) {
					if(cost[w] > cost[v]+cmap[v][w])
						cost[w] = cost[v]+cmap[v][w];
				}
			}
		}
	}
}

int main() {

	int i, j, n, m;
	int v, w, d, c;

	while(scanf("%d %d", &n, &m) != EOF) {
		if(n == 0 && m == 0) break;
		for(i = 1; i <= n; i++)
			for(j = 1; j <= n; j++)
				dmap[i][j] = cmap[i][j] = INF;

		for(i = 1; i <= m; i++) {
			scanf("%d %d %d %d", &v, &w, &d, &c);
			if(d < dmap[v][w] || (d == dmap[v][w] && c < cmap[v][w])) {
				dmap[v][w] = dmap[w][v] = d;
				cmap[v][w] = cmap[w][v] = c;
			}
		}

		scanf("%d %d", &v, &w);
		dijkstra(n, v);
		printf("%d %d\n", dist[w], cost[w]);
	}
	return 0;
}
