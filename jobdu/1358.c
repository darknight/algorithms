#include <stdio.h>

void bsort(int *p, int size) {

	int i, j, t;
	for(i = size - 1; i >= 0; i--)
		for(j = 0; j < i; j++) {
			if(p[j] > p[j+1]) {
				t = p[j];
				p[j] = p[j+1];
				p[j+1] = t;
			}
		}
}

int pack(int *p, int size, int sum) {

	int dp[100] = {0};
	int i, v;
	for(i = 0; i < size; i++)
		for(v = sum; v >= p[i]; v--)
			if(dp[v] < dp[v - p[i]] + p[i])
				dp[v] = dp[v - p[i]] + p[i];

	return dp[sum];
}

int check(long long n) {

	int sum = 0, t;
	int arr[10], size = 0;

	if(n < 10) return 0;
	while(n) {
		t = n % 10;
		arr[size++] = t;
		sum += t;
		n /= 10;
	}
	if(sum % 2) return 0;
	bsort(arr, size);
	sum /= 2;
	if(sum == pack(arr, size, sum))
		return 1;
	return 0;
}

int main() {

	long long low, high, count;

	while(scanf("%lld %lld", &low, &high) != EOF) {
		count = 0;
		while(low <= high) {
			if(check(low))
				count++;
			low++;
		}
		printf("%lld\n", count);
	}
	return 0;
}
