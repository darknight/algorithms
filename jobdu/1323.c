#include <stdio.h>

int main() {

	double game[3][3];
	double res, tmp;
	int index[3];
	char str[3] = {'W', 'T', 'L'};
	int i, j, k;
	for(i = 0; i < 3; i++) {
		tmp = 0;
		for(j = 0; j < 3; j++){
			scanf("%lf", &game[i][j]);
			if(game[i][j] > tmp) {
				tmp = game[i][j];
				index[i] = j;
			}
		}
	}
	for(i = 0; i < 3; i++)
		printf("%c ", str[index[i]]);
	res = (game[0][index[0]]*game[1][index[1]]*game[2][index[2]]*0.65 - 1)*2.0;
	printf("%.2lf\n", res);
}
