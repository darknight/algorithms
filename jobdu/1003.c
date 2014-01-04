#include <stdio.h>
#include <string.h>

int main() {

	char sa[15], sb[15];
	long long a, b;
	int i, len, neg;

	while(scanf("%s %s", sa, sb) != EOF) {
		a = b = 0;
		len = strlen(sa);
		neg = 0;
		for(i = 0; i < len; i++) {
			if(sa[i] == '-') neg = 1;
			else if(sa[i] != ',')
				a = a * 10 + sa[i] - '0';
		}
		if(neg) a = -a;
		len = strlen(sb);
		neg = 0;
		for(i = 0; i < len; i++) {
			if(sb[i] == '-') neg = 1;
			else if(sb[i] != ',')
				b = b * 10 + sb[i] - '0';
		}
		if(neg) b = -b;
		printf("%lld\n", a+b);
	}
	return 0;
}
