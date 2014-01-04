#include <stdio.h>
#define INF 0xFFFF

int main() {

	int i, n, m, cost[25];
	int dp[110];//optimized version...
	int v;
	while(scanf("%d", &m) != EOF) {
		scanf("%d", &n);
		for(i = 1; i <= n; i++)
			scanf("%d", &cost[i]);
		dp[0] = 0;
		for(v = 1; v <= m; v++)
			dp[v] = INF;
		for(i = 1; i <= n; i++)
			for(v = m; v >= cost[i]; v--)
				if(dp[v] > dp[v-cost[i]]+1)
					dp[v] = dp[v-cost[i]]+1;

		printf("%d\n", dp[m] == INF ? 0 : dp[m]);
	}
	return 0;
}
