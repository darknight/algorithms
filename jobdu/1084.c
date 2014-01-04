#include <stdio.h>

#define N 1000001
#define MOD 1000000000
int dp[N];
int main() {

	int i, n;
	while(scanf("%d", &n) != EOF) {
		dp[1] = 1;
		dp[2] = 2;
		for(i = 3; i <= n; i++) {
			if((i & 1) == 0)
				dp[i] = dp[i-1] + dp[i>>1];
			else
				dp[i] = dp[i-1];
			if(dp[i] > MOD)
				dp[i] -= MOD;
		}
		printf("%d\n", dp[n]);
	}
	return 0;
}
