#include "stdio.h"

int main(){
	int x, y;
	double z, salary;
	scanf("%d", &x);
	scanf("%d", &y);
	scanf("%lf", &z);
	salary = (y * z);
	printf("NUMBER = %d\n", x);
	printf("SALARY = U$ %.2lf\n", salary);
	return 0;
}
