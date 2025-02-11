#include "stdio.h"

int main(){
	int x, y, z, w, diference;
	scanf("%d", &x);
	scanf("%d", &y);
	scanf("%d", &z);
	scanf("%d", &w);
	diference = ((x * y) - (z * w));
	printf("DIFERENCA = %d\n", diference);
	return 0;
}
