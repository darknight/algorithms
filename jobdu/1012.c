#include <stdio.h>
#include <string.h>

int find(int idx, int set[]) {

	if(set[idx] == 0) return idx;
	else return find(set[idx], set);
}

void setUnion(int root1, int root2, int set[]) {

	int i, j;
	i = find(root1, set);
	j = find(root2, set);
	if(i != j)
		set[i] = j;
//	set[root2] = root1;
}

int main() {

	int set[1024], m, n;
	int i, j, k;
	int v, w;

	scanf("%d", &n);
	while(n) {
		scanf("%d", &m);
		memset(set, 0, 1024 * sizeof(int));
		for(i = 0; i < m; i++) {
			scanf("%d %d", &v, &w);
			setUnion(v, w, set);
		}
		k = 0;
		for(i = 1; i <= n; i++)
			if(set[i] == 0) k++;
		printf("%d\n", k-1);
		scanf("%d", &n);
	}
}
