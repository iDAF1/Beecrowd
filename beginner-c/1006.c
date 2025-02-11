#include "stdio.h"

int main(){
	double x, y, z, average;
	scanf("%lf", &x);
	scanf("%lf", &y);
	scanf("%lf", &z);
	average = ((x * 2) + ((y * 3) + z * 5)) / 10;
	printf("MEDIA = %.1lf\n", average);
	return 0;
}
