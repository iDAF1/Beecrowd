#include "stdio.h"

int main(){
	double x, y, average;
	scanf("%lf", &x);
	scanf("%lf", &y);
	average = ((x * 3.5) + (y * 7.5)) / 11;
	printf("MEDIA = %.5lf\n", average);
	return 0;
}
