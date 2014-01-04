#include <stdio.h>
#include <math.h>

int main() {
	int p,t,g1,g2,g3,gj;
	double final;
	
	while(scanf("%d %d %d %d %d %d", &p, &t, &g1, &g2, &g3, &gj) != EOF) {
		if(fabs(g1 - g2) <= t)
			final = (g1 + g2) / 2.0;
		else if(fabs(g3 - g1) <= t && fabs(g3 - g2) <= t) {
			final = g1 > g2 ? g1 : g2;
			final = final > g3 ? final : g3;
		}
		else if(fabs(g3 - g1) > t && fabs(g3 - g2) > t)
			final = gj;
		else if(fabs(g3 - g1) <= t)
			final = (g3 + g1) / 2.0;
		else
			final = (g3 + g2) / 2.0;

		printf("%.1f\n", final);
	}
}